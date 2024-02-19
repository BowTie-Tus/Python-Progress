import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()?"

string = lower + upper + number + symbol
length = 16
password = "".join(random.sample(string,length))

print("Your new password is " + password)

