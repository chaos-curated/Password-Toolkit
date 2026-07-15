password = input("Enter password: ")

score = 0

Upper_case = False
Lower_case = False
Digit = False
Special_char = False

# Length score
if len(password) >= 12:
    score += 2
elif len(password) >= 8:
    score += 1

# Check characters and add score
for ch in password:
    if ch.isupper() and not Upper_case:
        Upper_case = True
        score += 1

    elif ch.islower() and not Lower_case:
        Lower_case = True
        score += 1

    elif ch.isdigit() and not Digit:
        Digit = True
        score += 1

    elif not ch.isalnum() and not Special_char:
        Special_char = True
        score += 1

# Weak patterns
common = ["password", "password123", "123456", "12345678", "qwerty"]

if password.lower() in common:
    score = 0
elif len(set(password)) == 1:
    score -= 2
elif "1234" in password or "abcd" in password.lower() or "qwerty" in password.lower():
    score -= 1

# Tell user what is missing
missing = []

if not Upper_case:
    missing.append("Uppercase letter (A-Z)")

if not Lower_case:
    missing.append("Lowercase letter (a-z)")

if not Digit:
    missing.append("Digit (0-9)")

if not Special_char:
    missing.append("Special character (!@#$%^&*)")

if missing:
    print("\nMissing:")
    for item in missing:
        print("-", item)

# Final result
if score <= 2:
    print("\nWeak Password")
elif score <= 4:
    print("\nModerate Password")
elif score == 5:
    print("\nStrong Password")
else:
    print("\nVery Strong Password")