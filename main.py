import string
import random

def generate_password(length: int = 15):
  alphabet = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(alphabet) for i in range(length))
  return password

password = generated_password()
print(f"Generated Password: {password}")
