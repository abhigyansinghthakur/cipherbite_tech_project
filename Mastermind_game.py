import random

def generate_secret_number():
    # Generates a 4-digit random number as the secret number
    return random.randint(1000, 9999)

def get_player_guess():
    # Function to get valid guesses from the player
    while True:
        guess = input("Enter your guess (4-digit number): ")
        if guess.isdigit() and len(guess) == 4:
            return guess
        else:
            print("Please enter a valid 4-digit number.")

def check_guess(secret_number, guess):
    # Compares the guess with the secret number and provides hints
    if guess == secret_number:
        return "Correct"
    else:
        hint = []
        for i in range(4):
            if guess[i] == secret_number[i]:
                hint.append(guess[i])
            else:
                hint.append('*')
        return ''.join(hint)

def play_game():
    print("Welcome to the Mastermind Game!")
    print("Player 1 will set the secret number first.")

    # Player 1 sets the secret number
    secret_number_p1 = get_player_guess()

    # Player 2 attempts to guess Player 1's secret number
    attempts_p2 = 0
    while True:
        guess_p2 = get_player_guess()
        attempts_p2 += 1
        result = check_guess(secret_number_p1, guess_p2)
        print(f"Attempt {attempts_p2}: {guess_p2} -> {result}")
        if result == "Correct":
            print("Player 2 guessed the number correctly! Player 2 wins!")
            break

    # Player 2 has set the secret number, now Player 1 guesses
    print("\nNow, Player 2 will set the secret number and Player 1 will guess.")
    secret_number_p2 = get_player_guess()

    attempts_p1 = 0
    while True:
        guess_p1 = generate_secret_number()  # Generate a random guess for Player 1
        attempts_p1 += 1
        result = check_guess(secret_number_p2, guess_p1)
        print(f"Attempt {attempts_p1}: {guess_p1} -> {result}")
        if result == "Correct":
            print("Player 1 guessed the number correctly! Player 1 wins!")
            break

    # Determine the winner based on attempts
    if attempts_p1 < attempts_p2:
        print("Player 1 is crowned Mastermind!")
    elif attempts_p2 < attempts_p1:
        print("Player 2 is crowned Mastermind!")
    else:
        print("It's a draw!")

# Start the game
play_game()
