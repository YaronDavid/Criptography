package practicascrytpo;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Base64;
import java.util.Objects;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.KeyGenerator;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

public class AES {
    // KEY GENERATION
    public void keyGenerator() throws NoSuchAlgorithmException{
        String key256, key192, key128;
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(256);
        SecretKey secretKey = keyGen.generateKey();
        key256 = Base64.getEncoder().encodeToString(secretKey.getEncoded());
        
        keyGen.init(192);
        secretKey = keyGen.generateKey();
        key192 = Base64.getEncoder().encodeToString(secretKey.getEncoded());
        
        keyGen.init(128);
        secretKey = keyGen.generateKey();
        key128 = Base64.getEncoder().encodeToString(secretKey.getEncoded());

        guardarArchivo("Key256",key256);
        guardarArchivo("Key192",key192);
        guardarArchivo("Key128",key128);
        
    }    
    //**KEY GENERATION
    
    //TEST VECTOR
    //Obtained of https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf Apendix C 
    
    //**TEST VECTOR
    
    //CIPHER
    public void cipher(String keyFile256, String keyFile192, String keyFile128,String plainTextFile) throws UnsupportedEncodingException, NoSuchAlgorithmException, InvalidKeyException, NoSuchPaddingException, IllegalBlockSizeException, BadPaddingException, FileNotFoundException, IOException {
        String aux,contenido="";
        PrintWriter printWriter256 = null;
        PrintWriter printWriter192 = null;
        PrintWriter printWriter128 = null;
            try {
                printWriter256 = new PrintWriter("cipher256.txt");
                printWriter192 = new PrintWriter("cipher192.txt");
                printWriter128 = new PrintWriter("cipher128.txt");
            } catch (FileNotFoundException e){
                System.out.println("Unable to locate or to access the path :( " + e.getMessage());
            }
        //Obteniendo las llaves
        SecretKey key256 = ObtainKey(keyFile256); 
        SecretKey key192 = ObtainKey(keyFile192);
        SecretKey key128 = ObtainKey(keyFile128);
        //**Obteniendo las llaves
        
        //Obteniendo el texto
        FileReader g = new FileReader(plainTextFile+".txt");
        BufferedReader c = new BufferedReader(g);
        while((aux = c.readLine())!=null) {
          contenido = aux;
//CIFRADO      
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");        
            cipher.init(Cipher.ENCRYPT_MODE, key256);
            byte[] datosEncriptar = contenido.getBytes("UTF-8");
            byte[] bytesEncriptados = cipher.doFinal(datosEncriptar);
            String cipher256 = Base64.getEncoder().encodeToString(bytesEncriptados);
            
            cipher.init(Cipher.ENCRYPT_MODE, key192);
            byte[] datosEncriptar2 = contenido.getBytes("UTF-8");
            byte[] bytesEncriptados2 = cipher.doFinal(datosEncriptar2);
            String cipher192 = Base64.getEncoder().encodeToString(bytesEncriptados2);
            
            cipher.init(Cipher.ENCRYPT_MODE, key128);
            byte[] datosEncriptar3 = contenido.getBytes("UTF-8");
            byte[] bytesEncriptados3 = cipher.doFinal(datosEncriptar3);
            String cipher128 = Base64.getEncoder().encodeToString(bytesEncriptados3);
//CIFRADO            
            Objects.requireNonNull(printWriter256).println(cipher256);
            Objects.requireNonNull(printWriter192).println(cipher192);
            Objects.requireNonNull(printWriter128).println(cipher128);
        }
        printWriter256.close();
        printWriter192.close();
        printWriter128.close();
        c.close();
        //**Obteniendo el texto
    }
    //**CIPHER  
    
    //DECIPHER
     public void decipher(String keyFile256, String keyFile192, String keyFile128,String cipher256,String cipher192,String cipher128) throws UnsupportedEncodingException, NoSuchAlgorithmException, InvalidKeyException, NoSuchPaddingException, IllegalBlockSizeException, BadPaddingException, FileNotFoundException, IOException {
        String aux,contenido="";
        PrintWriter printWriter256 = null;
        PrintWriter printWriter192 = null;
        PrintWriter printWriter128 = null;
            try {
                printWriter256 = new PrintWriter("decipher256.txt");
                printWriter192 = new PrintWriter("decipher192.txt");
                printWriter128 = new PrintWriter("decipher128.txt");
            } catch (FileNotFoundException e){
                System.out.println("Unable to locate or to access the path :( " + e.getMessage());
            }
        //Obteniendo las llaves
        SecretKey key256 = ObtainKey(keyFile256); 
        SecretKey key192 = ObtainKey(keyFile192);
        SecretKey key128 = ObtainKey(keyFile128);
        //**Obteniendo las llaves
        
        //Obteniendo el texto
        FileReader g = new FileReader(cipher256+".txt");
        BufferedReader c = new BufferedReader(g);
        while((aux = c.readLine())!=null) {
            contenido = aux;
//DESCIFRADO  
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, key256);
            byte[] bytesEncriptados = Base64.getDecoder().decode(contenido);
            byte[] datosDesencriptados = cipher.doFinal(bytesEncriptados);
            String decipher256 = new String(datosDesencriptados);
//DESCIFRADO            
            Objects.requireNonNull(printWriter256).println(decipher256);
        }
        printWriter256.close();
        c.close();
        
        g = new FileReader(cipher192+".txt");
        c = new BufferedReader(g);
        while((aux = c.readLine())!=null) {
            contenido = aux;
//DESCIFRADO  
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, key192);
            byte[] bytesEncriptados = Base64.getDecoder().decode(contenido);
            byte[] datosDesencriptados = cipher.doFinal(bytesEncriptados);
            String decipher192 = new String(datosDesencriptados);
//DESCIFRADO            
            Objects.requireNonNull(printWriter192).println(decipher192);
        }
        printWriter192.close();
        c.close();
        
        g = new FileReader(cipher128+".txt");
        c = new BufferedReader(g);
        while((aux = c.readLine())!=null) {
            contenido = aux;
//DESCIFRADO  
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, key128);
            byte[] bytesEncriptados = Base64.getDecoder().decode(contenido);
            byte[] datosDesencriptados = cipher.doFinal(bytesEncriptados);
            String decipher128 = new String(datosDesencriptados);
//DESCIFRADO            
            Objects.requireNonNull(printWriter128).println(decipher128);
        }
        printWriter128.close();
        c.close();
        //**Obteniendo el texto
    }
    //**DECIPHER
    
    public void guardarArchivo(String nombreArchivo, String texto){
        PrintWriter printWriter = null;
            try {
                printWriter = new PrintWriter(nombreArchivo+".txt");
            } catch (FileNotFoundException e){
                System.out.println("Unable to locate or to access the path :( " + e.getMessage());
            }
            Objects.requireNonNull(printWriter).println(texto);
            printWriter.close();
    }
    
    public SecretKey ObtainKey(String keyFile) throws FileNotFoundException, IOException{
    String aux,key="";
        FileReader f = new FileReader(keyFile+".txt");
        BufferedReader b = new BufferedReader(f);
        while((aux = b.readLine())!=null) {
          key = key + aux;
        }
        b.close();
        byte[] decodedKey = Base64.getDecoder().decode(key);
        SecretKey result = new SecretKeySpec(decodedKey, 0, decodedKey.length, "AES"); 

    return result;
    }
    
    public void vectorPrueba(String key, String text) throws UnsupportedEncodingException, NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException{
            int len = key.length();
            byte[] data = new byte[len / 2];
            for (int i = 0; i < len; i += 2) {
             data[i / 2] = (byte) ((Character.digit(key.charAt(i), 16) << 4)
                             + Character.digit(key.charAt(i+1), 16));
            }
            
            System.out.println("Tam : "+data.length);
        for(int i=0;i<data.length;i++){
            System.out.println("data : "+data[i]);
        }

SecretKeySpec secretKey = new SecretKeySpec(data, "AES");
        
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");        
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);

        byte[] datosEncriptar = text.getBytes("UTF-8");
        byte[] bytesEncriptados = cipher.doFinal(datosEncriptar);
        String encriptado = Base64.getEncoder().encodeToString(bytesEncriptados);
        System.out.println("Prueba cifrada: "+encriptado);
      
        cipher.init(Cipher.DECRYPT_MODE, secretKey); 
        bytesEncriptados = Base64.getDecoder().decode(encriptado);
        byte[] datosDesencriptados = cipher.doFinal(bytesEncriptados);
        String datos = new String(datosDesencriptados);
        
        System.out.println("Prueba descifrada: "+datos);
    }
    
    
    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException, NoSuchPaddingException, IllegalBlockSizeException, BadPaddingException, FileNotFoundException, IOException {
        AES uno = new AES();
        uno.vectorPrueba("0000000000000000000000000000000000000000000000000000000000000000", "f34481ec3cc627bacd5dc3fb08f273e6");
//        uno.keyGenerator();
//        uno.cipher("Key256","key192","key128", "plainText");
//        uno.decipher("key256","key192","key128", "cipher256","cipher192","cipher128");
          
    }
}
