import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Common weak passwords list
    weak_patterns = [
        "123", "1234", "12345",
        "abc", "abcd",
        "qwerty",
        "password",
        "1111", "0000"
    ]

    # Check if password contains weak patterns
    for wp in weak_patterns:
        if wp in password.lower():
            return "Weak Password ❌\nReason: Contains common weak pattern → '" + wp + "'"

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Must contain at least one uppercase letter.\n"

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Must contain at least one lowercase letter.\n"

    # Digit check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "Must contain at least one digit.\n"

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "Must contain at least one special character.\n"

    # Final rating
    if strength == 5:
        return "Strong Password 💪"
    elif strength >= 3:
        return "Medium Password 😐\n" + remarks
    else:
        return "Weak Password ❌\n" + remarks


# -------- Main Program --------
password = input("Enter your password: ")
result = check_password_strength(password)
print("\nPassword Result:")
print(result)
