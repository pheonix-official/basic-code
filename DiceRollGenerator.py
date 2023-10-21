import numpy as np

def dice_roll():
    return np.random.randint(1, 7)

def play_dice_game():
    total_score = 0

    print("Welcome to the Dice Roll Game!")

    while True:
        current_roll = dice_roll()
        print(f"You rolled a {current_roll}")
        total_score += current_roll
        print(f"Your current total score is {total_score}")

        play_again = input("Do you want to roll again? (y/n): ")

        if play_again.lower() == "n":
            print(f"Thank you for playing! Your final score is {total_score}")
            break
        elif play_again.lower() != "y":
            print("Invalid input. Please enter y or n")

if __name__ == "__main__":
    play_dice_game()

   
