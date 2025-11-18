#Lana Hendrickson
#Module 3: Assignment - Secure Hashing and Encryption Cypher

#Varables/libaries
import random
FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1
fix = ""

def caesar_shift(message, shift):
    result = ""

    for char in message.upper():
        if char.isalpha():
            
            charCode = ord(char)
            newCharCode = charCode + shift
            
            if newCharCode > LAST_CHAR_CODE:
                newCharCode -= CHAR_RANGE
                
            
            if newCharCode < FIRST_CHAR_CODE:
                newCharCode += CHAR_RANGE
            
            newChar = chr(newCharCode)
            result += newChar
        else:
            result += char

    #output
    print(result)
    global fix
    fix = result
    
user_message = input("Please input a message: ")
user_shift_key = random.randint(1, 10)
caesar_shift(user_message, user_shift_key)
caesar_shift(fix, -user_shift_key)
