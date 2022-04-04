import random

r = int(input("Enter the number of rounds: "))
list = ["snake", "water", "gun"]
pointC = 0
pointM = 0
while r:
    r -= 1
    man1 = input("Enter your choice: ")
    man = man1.lower()
    comp = random.choice(list)
    print("Computer's choice is:", comp)
    if (
        (man == "snake" and comp == "water")
        or (man == "gun" and comp == "snake")
        or (man == "water" and comp == "gun")
    ):
        pointM += 1
    elif man == comp:
        pass
    else:
        pointC += 1

if pointM > pointC:
    print("Bingo!!! You have won")
elif pointC > pointM:
    print("Sorry, You have lost")
else:
    print("Scores tied.")
print("Points of computer:", pointC)
print("Your points:", pointM)