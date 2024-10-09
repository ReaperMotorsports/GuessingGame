#Christopher Morgan
#CIS 261
#GuessingGame

import random

#Part 1
print("Time to guess the number I'm thinking of!")

#Part 2
numberLimit = int(input("\nEnter the limit:     "))
print(f"I am thinking of a number between 1 and {numberLimit} ")
lowerEnd = 1
upperEnd = {numberLimit}
supriseNum = random.randint(lowerEnd, upperEnd)

chosenNum = int(input(f"\nGuess a number within specified range?     )
if {chosenNum} == {supriseNum}:
    print(f"\nNice job you guessed correctly!")

elif {chosenNum} > {supriseNum}:
    print(f"\nYour guess is too high, try again."

else:
    print(f"\nYour guess is too low, try again."

