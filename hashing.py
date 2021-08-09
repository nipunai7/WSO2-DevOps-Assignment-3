# Python program to demonstrate
# Linux Devops Training
 
 
import hashlib
import os

salt = hashlib.sha256(os.urandom(60)).digest().strip()

value = hashlib.pbkdf2_hmac('sha512',bytes(input("Input Value to be hashed: "),'utf-8'), salt, 200000).hex()
print (value) 
