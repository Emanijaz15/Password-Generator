import random
import string

user=int(input("Enter length of your password: "))
chars=string.ascii_letters + string.digits + string.punctuation
password=""
for i in range(user):
    password+=random.choice(chars)
print(password)
