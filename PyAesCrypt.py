import pyAesCrypt
from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "SelamCanım"

# encrypt
def encrypt():
    with open("tr.txt", "rb") as fIn:
        with open("data.txt.aes", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# get encrypted file size

# decrypt
def decrypt():
    encFileSize = stat("data.txt.aes").st_size
    with open("data.txt.aes", "rb") as fIn:
        try:
          with open("dataout.txt", "wb") as fOut:
            # decrypt file stream
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
        except ValueError:
        # remove output file on error
             remove("dataout.txt")


while True:
        choice = int(input(
            "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\nPress '5' to exit.\n"))
        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 5:
            exit()
        else:
            print("Please select a valid option!")