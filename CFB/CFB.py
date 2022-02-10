#Esquivel Ventura Yaron David

from random import randint
import math
#agregue los simbolos anteriores en UNICODE, para no tener problemas y tener 32 caracteres
alphabet = ["[","\\","]","^","_","`","a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l","m","n", "o", "p", "q", "r", "s","t","u", "v", "w", "x", "y", "z"]
#Establece el tamaño de a llave y el IV
tamanio = 20
def generate_key(length:int):
    key=[]
    for _ in range(length):
        key.append(randint(0,len(alphabet)))
    return key

def getBlockString(keyLength:int,text:str):
    blockString:list[str] = []
    for i in range(math.floor(len(text)/keyLength)):
        blockString.append(text[i*keyLength:keyLength*(i+1)])
    if(len(text)%keyLength!=0):
        lastLetters = text[keyLength*(i+1):]
        while(len(lastLetters)<keyLength):
            lastLetters+=alphabet[randint(0,len(alphabet))-1]
        blockString.append(lastLetters)
    return blockString

def cipher(key:list[str],plaintext:str):
    blockString = getBlockString(len(key),plaintext)
    cipherText =[]
    for i in range(len(blockString)):
        block = blockString[i]
        auxString = [""]*len(key)
        for j in range(len(block)):
            auxString[j]=alphabet[(alphabet.index(block[j])+key[j])%len(alphabet)]
        cipherText.append(auxString)
    textCipher = ""
    for i in range(len(cipherText)):
        for j in range(len(cipherText[i])):
            textCipher+=cipherText[i][j]
    return textCipher

def decipher(key:list[str],cipherText:str):
    blockString = getBlockString(len(key),cipherText)
    decipherText =[]
    for i in range(len(blockString)):
        block = blockString[i]
        auxString = [""]*len(key)
        for j in range(len(block)):
            auxString[j]=alphabet[(alphabet.index(block[j])-key[j])%len(alphabet)]
        decipherText.append(auxString)
    textDecipher = ""
    for i in range(len(decipherText)):
        for j in range(len(decipherText[i])):
            textDecipher+=decipherText[i][j]
    return textDecipher
    
#Cree la xor y la xor inversa
def sxor(s1,s2):
    ab=''
    for a,b in zip(s1,s2):
        auxi = ord(a) ^ ord(b)
        auxi = (auxi%len(alphabet))+91
        auxi = chr(auxi)
        ab = ab+auxi
    return ab

def sxorin(s1,s2):
    ab=''
    for a,b in zip(s1,s2):
        b = ord(b)-91
        auxi = ord(a) ^ b
        auxi = chr(auxi)
        ab = ab+auxi
    return ab

#Algoritmo de ciphrado y deciphrado CFB

def CFB(key, str1, IV):
    blocks = getBlockString(tamanio, str1)
    cipherText=""
    cipherblocks = []
    aux = []
    for i in range(len(blocks)):
        if(i==0):
            cipherblocks.append(sxor(blocks[i],IV))
        else:
            aux.append(cipher(key, cipherblocks[i-1]))
            cipherblocks.append(sxor(aux[i-1],blocks[i]))
        cipherText=cipherText+cipherblocks[i]
    return cipherText

def CFBdes(key, str1, IV):
    blocks = getBlockString(tamanio, str1)
    plainText=""
    plainBlock = []
    aux = []
    for i in range(len(blocks)):
        if(i==0):
            plainBlock.append(sxorin(IV,blocks[i]))
        else:
            aux.append(cipher(key,blocks[i-1]))
            plainBlock.append(sxorin(aux[i-1],blocks[i]))

        plainText=plainText+plainBlock[i]
    return plainText

#Generacion aleatoria de Vector de inicializacion

def generateIV(tamanio):
    IV=''
    for _ in range(tamanio):
        IV=IV+alphabet[randint(0,len(alphabet))-1]
    return IV

print("¿Qué quiere hacer?\nCifrar\nDecifrar")
action = input()
if(action=="Cifrar"):
    #cifrado

    key = generate_key(tamanio)
    IV = generateIV(tamanio)

    f = open ('texto.txt','r')
    texto = f.read()
    f.close()
    cipherText=''

    fi = open ('llave.txt','w')
    for i in key:
        fi.write(str(i)+' ')
    fi.close()

    fi = open('cifrado.txt','w')
    IV = cipher(key,IV)
    cipherText=IV+CFB(key,texto,IV)
    fi.write(cipherText)
    fi.close()
    print("Cifrado Exitoso")

#decifrado

if(action=="Decifrar"):

    f = open ('llave.txt','r')
    key = f.read()
    f.close()

    f = open ('cifrado.txt','r')
    texto = f.read()
    f.close()
    IV=''
    for i in range(tamanio):
        IV=IV+texto[i]
    texto=texto[tamanio:]
    llave = key.split(" ")
    llave.pop()
    key2 = []
    for i in llave:
        key2.append((int(i)))

    decipher = CFBdes(key2, texto, IV)
    f = open ('decifrado.txt','w')
    f.write(decipher)
    f.close()
    print("Texto decifrado")
