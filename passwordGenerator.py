import random
import string

user=int(input("Enter length of your password: "))
chars=string.ascii_letters + string.digits + string.punctuation
for i in range(user):
    print(random.choice(chars),end="")