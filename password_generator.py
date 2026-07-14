import random

length = int(input("Enter the length of the password: "))

c = input("Include uppercase letters? (T/F): ").capitalize()
d = input("Include lowercase letters? (T/F): ").capitalize()
e = input("Include digits? (T/F): ").capitalize()
f = input("Include special characters? (T/F): ").capitalize()

Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowercase = "abcdefghijklmnopqrstuvwxyz"
Digits = "0123456789"
Special_char = "!@#$%^&*"

character_pool = ""
password = ""
selected_types = 0

if c == "T":
    character_pool += Uppercase
    password += random.choice(Uppercase)
    selected_types += 1

if d == "T":
    character_pool += Lowercase
    password += random.choice(Lowercase)
    selected_types += 1

if e == "T":
    character_pool += Digits
    password += random.choice(Digits)
    selected_types += 1

if f == "T":
    character_pool += Special_char
    password += random.choice(Special_char)
    selected_types += 1

if selected_types == 0:
    print("Please select at least one character type.")
    raise SystemExit

if length < selected_types:
    print("Password length must be at least", selected_types)
    raise SystemExit

remaining = length - selected_types

for _ in range(remaining):
    password += random.choice(character_pool)

# Shuffle the password
password = list(password) #to convert password to list
random.shuffle(password) #to shuffle the list
password = "".join(password) #to convert list to password

print("Generated Password:", password)






        