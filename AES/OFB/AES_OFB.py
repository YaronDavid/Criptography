from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
"""
plain = open('text.txt','r')
text=plain.read()
plain.close()"""

def generateKeys():
    key1 = get_random_bytes(16)
    auxk = base64.b64encode(key1)
    key128 = open('key128.txt', 'w')
    key128.write(auxk.decode("utf-8"))
    key128.close()

    key2 = get_random_bytes(24)
    auxk = base64.b64encode(key2)
    key192 = open('key192.txt', 'w')
    key192.write(auxk.decode("utf-8"))
    key192.close()

    key3 = get_random_bytes(32)
    auxk = base64.b64encode(key3)
    key256 = open('key256.txt', 'w')
    key256.write(auxk.decode("utf-8"))
    key256.close()

def EncriptCFB(plain:str, key:str):
    key = key.encode("utf-8")
    key = base64.b64decode(key)
    j=0
    for i in key:
        j=j+1
    iv = get_random_bytes(16)
    plain = plain.encode("utf-8")
    aes = AES.new(key, AES.MODE_OFB, iv)
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
    other = AES.new(key, AES.MODE_OFB, iv)
    decoded = other.decrypt(cipher)
    decoded = decoded.decode("utf-8")
    decipher = open('decipher'+str(j*8)+'.txt','w')
    decipher.write(decoded)
    decipher.close()

def EncriptExampleVectorsCFB(plain, key, iv, predict, mode):
    j=0
    for i in key:
        j=j+1
    aes = AES.new(key, AES.MODE_OFB, iv)
    print("key "+str(j*8)+": "+key.hex())
    print("iv: "+iv.hex())
    if mode == "en":
        cipher = aes.encrypt(plain)
        print("plain: "+plain.hex())
        print("cipher: "+cipher.hex())
    if mode == "de":
        cipher = aes.decrypt(plain)
        print("cipher: "+plain.hex())
        print("plain: "+cipher.hex())
    print("predict "+predict)
    print("==================================================================================")


#algorithm for Encript and Decript a File text
"""
generateKeys()
k128 = open('key128.txt','r')
key1 = k128.read()
k128.close()

k192 = open('key192.txt','r')
key2 = k192.read()
k192.close()

k256 = open('key256.txt','r')
key3 = k256.read()
k256.close()

EncriptCFB(text,key1)
EncriptCFB(text,key2)
EncriptCFB(text,key3)

r1 = open('cipher128.txt','r')
cipher = r1.read()
DecryptCFB(cipher, key1)

r2 = open('cipher192.txt','r')
cipher = r2.read()
DecryptCFB(cipher, key2)

r3 = open('cipher256.txt','r')
cipher = r3.read()
DecryptCFB(cipher, key3)

r1.close()
r2.close()
r3.close()"""

#Test Vectors

key = "2b7e151628aed2a6abf7158809cf4f3c"
iv = "000102030405060708090a0b0c0d0e0f"
text = "6bc1bee22e409f96e93d7e117393172a"
predict = "3b3fd92eb72dad20333449f8e83cfb4a"

EncriptExampleVectorsCFB(bytes.fromhex(text), bytes.fromhex(key), bytes.fromhex(iv), predict, "en")
EncriptExampleVectorsCFB(bytes.fromhex(predict), bytes.fromhex(key), bytes.fromhex(iv), text, "de")

key = ' 8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b'
predict = "cdc80d6fddf18cab34c25909c99a4174"

EncriptExampleVectorsCFB(bytes.fromhex(text), bytes.fromhex(key), bytes.fromhex(iv), predict, "en")
EncriptExampleVectorsCFB(bytes.fromhex(predict), bytes.fromhex(key), bytes.fromhex(iv), text, "de")

key = "603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
predict = "dc7e84bfda79164b7ecd8486985d3860"

EncriptExampleVectorsCFB(bytes.fromhex(text), bytes.fromhex(key), bytes.fromhex(iv), predict, "en")
EncriptExampleVectorsCFB(bytes.fromhex(predict), bytes.fromhex(key), bytes.fromhex(iv), text, "de")