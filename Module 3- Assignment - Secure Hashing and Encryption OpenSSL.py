#Lana Hendrickson
#Module 3: Assignment - Secure Hashing and Encryption OpenSSL

#Varables/libaries
import hashlib


#input
string = input("Please input a message: ")

result = hashlib.sha256(string.encode())

#output
print(result.hexdigest)