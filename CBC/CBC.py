#Esquivel Ventura Yaron David
from random import randint
import math
import tkinter
from tkinter import filedialog
from tkinter import messagebox

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x','y','z',' ',',','\n', '.','?','!' ]
def generate_random_string(length:int): #funcion generadorea de la llave y el IV
    word=[]
    for _ in range(length):
        word.append(alphabet[randint(0,len(alphabet)-1)])
    return ''.join(word)
def get_blockString(length:int,text:str): #Particion del texto a cifrar o descifrar
    blockString:list[str] = []
    for i in range(math.floor(len(text)/length)):
        blockString.append(text[i*length:length*(i+1)])
    if(len(text)%length!=0):
        lastLetters = text[length*(i+1):]
        while(len(lastLetters)<length):
            lastLetters+=alphabet[alphabet.index(' ')]
        blockString.append(lastLetters)
    return blockString
def cipher(key:list[str],block:str)->str: #Cifrado vigenère
    txtciphered=""
    for i in range(len(block)):
        txtciphered+=alphabet[(alphabet.index(block[i])+alphabet.index(key[i]))%(len(alphabet))]
    return txtciphered
def decipher(key:list[str],ciphertxt:str)-> str: #Descifrado vigenère
    normaltxt=""
    for i in range(len(ciphertxt)):
        aux= alphabet.index(ciphertxt[i])-alphabet.index(key[i])
        if(aux<0):
            aux= len(alphabet)-((-1)*aux)%len(alphabet)
        normaltxt+=alphabet[aux%len(alphabet)]
    return normaltxt
def xor_operation(block1:str, block2:str)->str: #operación xor entre 2 bloques y obtención de su representación en el diccionario
    result=""
    for i in range(len(block1)):
        block1numrep=alphabet.index(block1[i])
        block2numrep=alphabet.index(block2[i])
        result+=alphabet[block1numrep^block2numrep]
    return result
def cbc_cipher(blocks: list, iv:str, key: str)->list: #Cifrado vigenère con el modo de operación CBC
    firstblock=blocks[0]
    blocks.remove(firstblock)
    firstxor= xor_operation(iv,firstblock)
    blocksciphered=[]
    blocksciphered.append(cipher(key,firstxor))
    for i in range(len(blocks)):
        blockxored= xor_operation(blocksciphered[i], blocks[i])
        blocksciphered.append(cipher(key, blockxored))
    return blocksciphered
def cbc_decipher(blocksciphered: list, iv:str, key:str)->list: #Descifrado vigenère con el modo de operación CBC
    blocksdeciphered=[]
    firstdeciphered=decipher(key,blocksciphered[0])
    blocksdeciphered.append(xor_operation(iv, firstdeciphered))
    for i in range (1,len(blocksciphered)):
        block= decipher(key, blocksciphered[i])
        blocksdeciphered.append(xor_operation(blocksciphered[i-1], block))
    return blocksdeciphered
def write_onfile(data: str): #escritura en el archivo
    arcnom=filedialog.asksaveasfile(mode="w").name #guardado de llavea
    archivo=open(arcnom,"w")
    archivo.write(data)
    archivo.close()
def get_filename()->str: #creación y obtención de la ruta absoluta donde se guardará un archivo
    txtnom=filedialog.askopenfile().name#selección de archivo de texto a encriptar
    return txtnom
def get_data(filename: str)->str: #lectura de datos
    file=open(filename,"r")
    data=file.read()
    return data
if  __name__ == "__main__": #main
    root = tkinter.Tk()
    root.withdraw()
    # #Inicio generación de llave y de Vector de inicialización
    # tamkey= int(input("Ingresa el tamaño de la llave para el cifrado Vigenère: "))
    # tamiv=tamkey
    # iv=generate_random_string(tamiv)
    # key=generate_random_string(tamkey)
    # print(key)
    # print(iv)
    # messagebox.showinfo("Mensaje", "Seleccione la localización donde quiera guardar la llave")
    # write_onfile(''.join(key))
    # messagebox.showinfo("Mensaje", "Seleccione donde quiera guardar el vector de inicialización")
    # write_onfile(''.join(iv))
    # Fin
    #Inicio lectura de archivo, cifrado
    # messagebox.showinfo("Mensaje", "Seleccione la localización de la llave")
    # keyfilename= get_filename()
    # key=get_data(keyfilename)
    # messagebox.showinfo("Mensaje", "Seleccione la localización del Vector de inicialización")
    # ivfilename=get_filename()
    # iv=get_data(ivfilename)
    # tamiv=tamkey=len(key)
    # messagebox.showinfo("Mensaje", "Seleccione el archivo a cifrar")
    # nametxttocipher=get_filename()
    # datatxttocipher=get_data(nametxttocipher)
    # blocks= get_blockString(tamkey, datatxttocipher)
    # blocksciphered=cbc_cipher(blocks, iv, key)
    # messagebox.showinfo("Mensaje", "Seleccione donde guardar el cifrado")
    # write_onfile(''.join(blocksciphered))
    # messagebox.showinfo("Mensaje", "Archivo cifrado con éxito usando Vigenerè y el modo de operación CBC")
    # #fin
    #Inicio descifrado
    # messagebox.showinfo("Mensaje", "Seleccione la localización de la llave")
    # keyfilename= get_filename()
    # key=list(get_data(keyfilename).strip(' '))
    # messagebox.showinfo("Mensaje", "Seleccione la localización del Vector de inicialización")
    # ivfilename=get_filename()
    # iv=list(get_data(ivfilename).strip(' '))
    # tamiv=tamkey=len(key)
    # messagebox.showinfo("Mensaje", "Seleccione el archivo a decifrar")
    # nametxttodecipher=get_filename()
    # datatxttodecipher=get_data(nametxttodecipher)
    # blocksciphered= get_blockString(tamkey, datatxttodecipher)
    # blocksdeciphered= cbc_decipher(blocksciphered, iv, key)
    # messagebox.showinfo("Mensaje", "Seleccione donde guardar el descifrado")
    # write_onfile(''.join(blocksdeciphered))
    # messagebox.showinfo("Mensaje", "Archivo decifrado con éxito ")
    #fin