import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
lower_case = list(lower_case)
rand_lower = random.choice(lower_case)

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upper_case = list(upper_case)
rand_upper = random.choice(upper_case)

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number = str(random.randint(0, 10))

symbols = ['#', '$', '@', '*', '_', '!', '%', '&', '^', '-', '+', '/', '?']
symbol = random.choice(symbols)

elements = lower_case + upper_case + numbers + symbols

password_length = int(input("Enter password length: "))

password = rand_lower + rand_upper + number + symbol
password = [i for a, i in enumerate(password)]

password += random.choices(elements, k=password_length - 4)
random.shuffle(password)

print(''.join(i for i in password))
