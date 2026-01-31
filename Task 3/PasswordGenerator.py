
import random
import string

password_length = int(input("Enter the length of the password: "))

characters = string.ascii_letters + string.digits + string.punctuation 

Generated_password = ""

for i in range(password_length):
    Generated_password += random.choice(characters)

print("My Password is:", Generated_password)
