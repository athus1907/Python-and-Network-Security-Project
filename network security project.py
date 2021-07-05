#Program to generate MD5 of  string data

import hashlib

name = input("Enter your value:")#taking input from user
md5_result = hashlib.md5(name.encode())

print('md5 value is->')
print(md5_result.hexdigest())
