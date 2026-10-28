import random

WORDS = ["python", "hangman", "keyboard", "program", "computer"]
MAX_WRONG = 6


def show_progress(word, guessed):
    """Return the word with unguessed letters hidden, e.g. p _ t h _ n"""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []          # all letters the player has tried
    wrong = 0

    print("=== HANGMAN ===")
    print(f"I'm thinking of a {len(word)}-letter word. You have {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print("Word:", show_progress(word, guessed))
        print("Guessed:", " ".join(sorted(guessed)) if guessed else "-")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        guess = input("Enter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong += 1
            print("Wrong guess!\n")

        # Win check: every letter of the word has been guessed
        if all(letter in guessed for letter in word):
            print("Word:", show_progress(word, guessed))
            print(f"Congratulations, you won! The word was '{word}'.")
            return

    print(f"Game over! You ran out of guesses. The word was '{word}'.")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
