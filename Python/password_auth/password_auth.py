---
Author: Gbenga Ojo
Date: 10.28.26
----

# A simple script to check for password validation

import string

def check_password(password):
    checks = {
        "At least 12 characters": len(password) >= 12,
        "Contains an uppercase letter": any(c.isupper() for c in password),
        "Contains a lowercase letter": any(c.islower() for c in password),
        "Contains a number": any(c.isdigit() for c in password),
        "Contains a symbol": any(c in string.punctuation for c in password),
    }

    for requirement, passed in checks.items():
        print(f"{requirement}: {'PASS' if passed else 'FAIL'}")

check_password("ExamplePass123!")
