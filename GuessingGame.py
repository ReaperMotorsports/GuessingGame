#Christopher Morgan
#CIS 261
#GuessingGame

import random

#Part 1
print("Time to guess the number I'm thinking of!")

#Part 2
keepPlaying = "y"
while keepPlaying.lower() == "y":
    
    numberLimit = int(input("\nEnter the limit:     "))
    print(f"I am thinking of a number between 1 and {numberLimit} ")
    supriseNum = random.randint(1,numberLimit)
    chosenNum = int(input("Guess a number within specified range:     "))
    while chosenNum != supriseNum:

    
    
        if chosenNum < supriseNum:
            print(f"Your guess is too low, try again")
            chosenNum = int(input("Your guess:     "))

        elif chosenNum > supriseNum:
            print(f"Your guess is too high, try again")
            chosenNum = int(input("Your guess:    "))

        else:
            break
 
    print("Your guess is correct. Nice job!")
    keepPlaying = input(f"\nWould you like to play again? (y/n):     ")
print(f"\nGood Bye.")