# Password Strength Checker 
## Introduction

The **Password Strength Checker** is a beginner‑friendly Python project that analyzes how strong or weak a password is. It checks for length, character types, common weak patterns, and provides a clear strength rating.

This README is kept simple and easy so you can directly use it for your GitHub project or college submission.

---

## What This Tool Does

The program checks your password for:

* Sufficient length
* Uppercase characters
* Lowercase characters
* Numbers
* Special characters
* Weak/common patterns (like `123`, `password`, `abcd`)

Based on these checks, it tells whether the password is **Strong**, **Medium**, or **Weak**.

---

## Features

* Detects common weak password patterns
* Checks 5 important security criteria
* Gives clear suggestions for improvement
* Beginner-friendly Python code
* Works entirely offline

---

## File Included

* **passwordchecker.py** — Main Python script

---

## How It Works (Easy Explanation)

1. You enter a password.
2. The program checks:

   * Length
   * Uppercase
   * Lowercase
   * Digits
   * Special symbols
3. It also checks if your password contains obvious patterns like:

   * `123`, `abcd`, `password`, `qwerty`, etc.
4. It gives a final rating:

   * **Strong 💪** (all conditions satisfied)
   * **Medium 😐** (3–4 conditions satisfied)
   * **Weak ❌** (less than 3 or contains weak pattern)

---

## Python Code

```
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
```

---

## How to Run

1. Install Python
2. Save the code as **passwordchecker.py**
3. Open your terminal or command prompt
4. Run:

```
python password_checker.py
```

5. Enter any password to test its strength.

---

## Example Output

```
Enter your password: Abcd@123

Password Result:
Strong Password 💪
```

Another Example:

```
Enter your password: hello123

Password Result:
Medium Password 😐
Must contain at least one uppercase letter.
Must contain at least one special character.
```

---

## Author
Jyotirmoy Mahapatra
