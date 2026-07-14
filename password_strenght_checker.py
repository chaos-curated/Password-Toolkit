password = input("Enter password: ")

score = 0

Upper_case = False
Lower_case = False
Digit = False
Special_char = False

# Length
if len(password) >= 12:
    score += 2
elif len(password) >= 8:
    score += 1

# Check characters
for ch in password:
    if ch.isupper():
        Upper_case = True
    elif ch.islower():
        Lower_case = True
    elif ch.isdigit():
        Digit = True
    else:
        Special_char = True

# Add score
if Upper_case:
    score += 1
if Lower_case:
    score += 1
if Digit:
    score += 1
if Special_char:
    score += 1

# Weak patterns
common = ["password", "password123", "123456", "12345678", "qwerty"]

if password.lower() in common:
    score = 0
elif len(set(password)) == 1:
    score -= 2
elif "1234" in password or "abcd" in password.lower() or "qwerty" in password.lower():
    score -= 1

# Result
if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Moderate Password")
elif score == 5:
    print("Strong Password")
else:
    print("Very Strong Password")