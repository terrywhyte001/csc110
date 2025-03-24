# step 1 : store the secret word (mosiah) in a variable
secret_word = "mosiah"

def generate_hint():
    hint = "book of mormon"
    return hint
    return "------"

def check_guess(guess):
    return guess == secret_word

def update_hint(hint, guess):
    new_hint = "a king in the Book of Mormon"
    return new_hint

def main():
    hint = generate_hint()
    print("Welcome to the guessing game")
    print("Guess the secret word")
    print ("Hint: " + hint)
    attempt = 0

    while attempt < 3:
        guess = input("Enter your guess: ")
        if check_guess(guess):
            print("You guessed the secret word")
            break
        else:
            hint = update_hint(hint, guess)
            print("Hint: " + hint)
            attempt += 1
            if attempt == 3:
                print("You've used all attempts. The secret word was:", secret_word)

main()

