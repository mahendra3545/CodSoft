'''Date:25 November 2023
Author:Mahendra pratap singh
Programme: Password generator '''
import random
import string

def generate_password(length=8):
    password = ""
    for _ in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

password = generate_password()
print(f"Your generated password is: {password}")