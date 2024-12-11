import random

def random_number_guess():
    print("Hello, welcome to the game!")
    score = {"wins": 0, "losses": 0}

    print("\nPlease choose from one of the options below...")
    print("1. Play the game")
    print("2. See your score")
    print("3. Exit the game...")
    choice = input("Pick a number between 1 and 3: ")
    
  
    if choice == "1":
        userGuess = usersGuess()
        compGuess = computersGuess()
        if userGuess == compGuess:
            print("Well done you guessed correctly!")
            score["wins"] += 1
        else:
            print("Uh oh, you lost. Loser!")
            score["losses"] += 1
    elif choice == "2":
        print(f"Wins: {score['wins']}, Losses: {score['losses']}")
    elif choice == "3":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


def usersGuess():
    guess = input("Pick a number between 1 and 10...")
    return guess

def computersGuess():
    return random.randint(1, 10)
    
def main():
    random_number_guess()
if __name__ == "__main__":
    main()