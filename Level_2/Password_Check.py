import re

def check_password_strength(password):

    uppercase = re.compile(r'[A-Z]')
    lowercase = re.compile(r'[a-z]')
    digit = re.compile(r'\d')
    special = re.compile(r'[!@#$%^&*()\-_=+{};:,<.>/?]')

    # Initialize strength score
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase letter check
    if uppercase.search(password):
        score += 1

    # Lowercase letter check
    if lowercase.search(password):
        score += 1

    # Digit check
    if digit.search(password):
        score += 1

    # Special character check
    if special.search(password):
        score += 1

    # Determine strength level based on score
        
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"


# Main Code
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)
