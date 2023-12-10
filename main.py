import random
words = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len_pass = int(input('Select length of password'))
password = ''
for i in range(len_pass):
    password += random.choice(words)
print(password)