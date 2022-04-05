"""
Exercise 2 - Faulty Calculator
45 * 3 = 555, 56+9 = 77, 56/6 = 4
Design a calculator which will correctly solve all the problems except
the following ones:
45 * 3 = 555, 56+9 = 77, 56/6 = 4
Your program should take operator  and the two numbers as input from the user
and then return the result
"""

a = input("Enter the first number: ")
c = input("Eneter the operator: ")
b = input("Enter the secont number: ")

func = a + c + b
reverse = b + c + a

faults = {"45*3": "555", "56+9": "77", "56/6": "4"}

if func in faults.keys():
    print(faults[func])
elif reverse in faults.keys():
    print(faults[reverse])
else:
    print(eval(func))
