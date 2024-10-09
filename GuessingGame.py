#Christopher Morgan
#CIS 261
#GuessingGame

import random

#Part 1
print("Time to guess the number I'm thinking of!")

#Part 2

numberLimit = int(input("\nEnter the limit:     "))
print(f"I am thinking of a number between 1 and {numberLimit} ")
supriseNum = random.randint(1,numberLimit)
print(f"{supriseNum}")
chosenNum = int(input("Guess a number within specified range?"))
while chosenNum != supriseNum:

    
    
    if chosenNum < supriseNum:
        print("Your guess is too low, try again")

    elif chosenNum > supriseNum:
        print("Your guess is too high, try again.")

    else:
        print("Your guess is correct. Nice job!")


