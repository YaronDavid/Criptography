from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def generateKeys():
    key = get_random_bytes(16)
    auxk = base64.b64encode(key)
    key128 = open('key128.txt', 'w')
    key128.write(auxk.decode("utf-8"))
    key128.close()

def EncriptCFB(plain:str, key:str):
    key = key.encode("utf-8")
    key = base64.b64decode(key)
    j=0
    for i in key:
        j=j+1
    iv = get_random_bytes(16)
    plain = plain.encode("utf-8")
    aes = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    cipher = aes.encrypt(plain)
    cipher = base64.b64encode(cipher)
    cipher = cipher.decode("utf-8")
    iv = base64.b64encode(iv)
    iv = iv.decode("utf-8")
    cipher = iv+cipher
    ci = open('cipher'+str(j*8)+'.txt','w')
    ci.write(cipher)
    ci.close()

def DecryptCFB(cipher:str, key:str):
    j=0
    key = key.encode("utf-8")
    key = base64.b64decode(key)
    for i in key:
        j=j+1
    iv = cipher[:24]
    cipher = cipher[24:]
    cipher = cipher.encode("utf-8")
    cipher = base64.b64decode(cipher)
    iv = iv.encode("utf-8")
    iv = base64.b64decode(iv)
    other = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    decoded = other.decrypt(cipher)
    decoded = decoded.decode("utf-8")
    decipher = open('decipher'+str(j*8)+'.txt','w')
    decipher.write(decoded)
    decipher.close()

print("Elige una opcion")
print("1.-Cifrar rexto")
print("2.-Decifrar texto")
i = input()



if(i=="1"):
    plain = open('text.txt','r')
    text=plain.read()
    plain.close()
    generateKeys()

    k128 = open('key128.txt','r')
    key = k128.read()
    k128.close()

    EncriptCFB(text,key)

if(i=="2"):
    k128 = open('key128.txt','r')
    key = k128.read()
    k128.close()
    
    r1 = open('cipher128.txt','r')
    cipher = r1.read()
    r1.close()

    DecryptCFB(cipher, key)