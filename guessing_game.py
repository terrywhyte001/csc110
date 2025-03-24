# step 1 : store the secret word (mosiah) in a variable
secret_word = "mosiah"

def providehint(secret_word, guess):
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())  # correct letter and position
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())  # correct letter but wrong position
        else:
            hint.append("_")  # letter not in the word
    return " ".join(hint)

def word_guessing_game():
    secret_word = "mosiah"
    attempts = 0
    print("Welcome to the guessing game")
    print(f"Try to guess the {len(secret_word)}-letter word")
    print("_ " * len(secret_word))  # initial hint display

    while True:
        guess = input("Enter your guess: ").strip().lower()
        attempts += 1
        if len(guess) != len(secret_word):
            print(f"Please enter a {len(secret_word)}-letter word.")
            continue
        if guess == secret_word:
            print(f"Congratulations! You guessed the secret word in {attempts} attempts")
            break
        hint = providehint(secret_word, guess)
        print(f"Hint: {hint}")

if __name__ == "__main__":
    word_guessing_game()
