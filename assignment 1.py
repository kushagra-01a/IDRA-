import random

def play_guessing_game():
    # 1. Configuration (You can change these values easily)
    min_num = 1
    max_num = 100
    max_attempts = 7
    
    # 2. Generate the random number
    secret_number = random.randint(min_num, max_num)
    
    print("Welcome to the Number Guessing Game!")
    print(f"I am thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("-" * 30)

    # 3. Game Loop (fixed number of attempts)
    for attempt in range(1, max_attempts + 1):
        # Input validation to ensure the user actually types a number
        while True:
            try:
                guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
                break # Exit the input loop if a valid number is entered
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        # 4. Conditional logic for feedback
        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            # 5. Success Message
            print(f"🎉 Congratulations! You guessed the number in {attempt} attempts!")
            return # Exits the function and ends the game successfully
    
    # 6. Failure Message (Only runs if the loop finishes without a correct guess)
    print(f"Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}. Better luck next time!")

# Start the game when the file is run
if __name__ == "__main__":
    play_guessing_game()
