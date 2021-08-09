# Python program to demonstrate
# Linux Devops Training


import hashlib
import os

salt = hashlib.sha256(os.urandom(60)).digest().strip()

value = hashlib.sha512(salt+bytes(input("Enter the value to be hashed: "),'utf-8')).hexdigest()
print (value)
