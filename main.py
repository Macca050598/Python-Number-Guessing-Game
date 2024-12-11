#1. Number Guessing Game
#A simple game where the computer randomly selects a number within a range, and the player has to guess it.
#Add features like giving hints (higher/lower) or limiting the number of attempts.
import random
def random_guess_game():
    print("Hey, welcome to my game!")
    print("\nPlease choose an option below...")
    print("1. Play the game")
    print("2. Check your score")
    print("3. Exit the game...")
    choice = input("Please choose a number 1-3: ")
    score = {"Wins": 0 , "Losses": 0}

    if choice == "1":
        yourGuess = users_guess()    
        computerGuess = computers_guess()
        if yourGuess == computerGuess:
            print("Well done you got it right")
            score["Wins"] += 1
        else:
            print("Uh oh the computer won")
            score["Losses"] += 1    
    elif choice == "2":
        print(("wins"), score["Wins"], ("Losses"), score["Losses"])
    elif choice == "3":
            print("Exiting the game...")
    return  
def users_guess():
        print("Please choose a number from 1 - 10")
        guess = input("Please choose a number")
        return guess
        
def computers_guess():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] 
    return random.choice(numbers)
        
        
def main():
    random_guess_game()
#Doesnt run the main function unless we choose an option 
if __name__ == "__main__":
    main()