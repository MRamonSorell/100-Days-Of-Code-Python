
# M.R. Sorell
# Project Python password generator
# letters : ask how many letters
# numbers : ask how many numbers
# symbols : ask how many symbols

# generate a random password

import random

print("Welcome to the password generator")

letters = int(input("How many letters do you want in your password: "))
integers = int(input("How many numbers do you want in your password: "))
symbols = int(input("How many symbols do you want in your password: "))

count = letters + integers + symbols

alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_code = list(alphabet)

numbers = "123456789"
num_code = list(numbers)

special = "$%&?!+"
special_code = list(special)

alpha = random.sample(alpha_code, letters)
nums  = random.sample(num_code, integers)
symbols = random.sample(special_code, symbols)

new_string = alpha + nums + symbols


# can use the random shuffle function
password = random.sample(new_string, count)

sep = ""
password_result = sep.join(password)

print(password_result)


print(f"Your new password is {password_result}")