import numpy as np
from random import  random
#Random dice roll generator
def dice_roll():
    dice = np.random.randint(1,7)
    return dice
print(dice_roll())
while True:
    play_again = input("Do you want to roll again? (y/n): ")
    if play_again == "y":
        print(dice_roll())
    elif play_again == "n":
        print("Thank you for playing")
        break
    else:
        print("Invalid input. Please enter y or n")
        continue


   