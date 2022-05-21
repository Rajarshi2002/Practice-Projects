"""Problem Statement:- Generate a random integer from a to b. You and your friend have to guess a number between two
numbers, a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to
keep choosing the number, and your program must tell whether the number is greater than the actual number or less
than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game,
and then the person with the minimum number of trials wins! Randomly generate a number after taking a and b as input
and don’t show that to the user.

Input:
Enter the value of a
4
Enter the value of b
13

Output:
Player1 :
Please guess the number between 4 and 13
5
Wrong guess a greater number again
8
Wrong guess a smaller number again
6
Correct, you took 3 trials to guess the number

Player 2:
Correct, you took 7 trials to guess the number
Player 1 wins!
"""

import random

a = int(input("Enter the value of lower limit: "))
b = int(input("Enter the value of upper limit: "))
r = random.randint(a, b+1)
Player1 = 0
Player2 = 0

for _ in range(2):
    print(f"It's Player{_+1}'s Turn:-")
    print(f"Please guess the number between [{a}, {b}]")
    i = 0
    while True:
        g = int(input())
        if g == r:
            print(f"Correct, you took {i+1} trials to guess the number")
            break
        elif g < r:
            print("Wrong guess, you entered a smaller number")
            print(f"{i + 1} chances taken")
            i += 1
        else:
            print("Wrong guess, you entered a greater number")
            print(f"{i + 1} chances taken")
            i += 1
    if _ == 0:
        Player1 = i
    else:
        Player2 = i

if Player1 < Player2:
    print("Player1 Won !!!")
elif Player1 == Player2:
    print("It's a Draw")
else:
    print("Player2 Won !!!")