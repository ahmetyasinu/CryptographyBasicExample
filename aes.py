from Crypto.Cipher import AES
import hashlib
import os

password = b'Ega.123'
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = 'This is an IV456'
file='./tr.txt'

def pad_message(file):
    while len(file) % 16 != 0:
        file = file + b'0'
    return file
    
pad_message(file)


cipher = AES.new(key, mode, IV)

with open('./tr.txt','rb') as f:
    orig_file = f.read()


padded_file = pad_message(orig_file)


encrypted_message = cipher.encrypt(padded_file)

with open('/tr.txt.env', 'wb')as e:
    e.write(encrypted_message)