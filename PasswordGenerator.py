import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the required length of the password(Maximum 20): "))
if (password_length>0 and password_length<=20):
  password = generate_password(password_length)
  print("Generated Password:", password)
elif password_length >20:
  print("Password length should be less than 20")
elif password_length ==0:
  print("Password length should be greater than 0")
else:
  print("Invalid Password Length")