import random

# Exercise 3: Number Guessing Game (Simplified)

# Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

print("--- Welcome to the Guessing Game! ---")
print("I'm thinking of a number between 1 and 10.")

guess = 0

# Loop until the user guesses the correct number
while guess != secret_number:
    user_input = input("\nEnter your guess: ")
    
    # Direct conversion (will fail if not a number)
    guess = int(user_input)
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the secret number!")

print("Thanks for playing!")
