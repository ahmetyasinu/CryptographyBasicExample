from fileenc_openssl import stretch_key , encrypt_file 
from fileenc_openssl import decrypt_file
sifre = stretch_key("123sifre123")

def encrypt():
    encrypt_file("/home/ega/Desktop/tr.txt" , key = sifre)
def decrypt():
    decryptf = decrypt_file("/home/ega/Desktop/tr.txt.enc", key = sifre)
    print("Desifrelenmis Dosya: " , decrypt_file("/home/ega/Desktop/tr.txt.enc", key = sifre ))
try:
    dosya = open(decrypt_file("/home/ega/Desktop/tr.txt.enc", key = sifre ) , "r" , encoding = "utf-8")
    for i in dosya:
        print (i)
except FileNotFoundError:
    print("Dosya bulunamadi.")
decrypt()