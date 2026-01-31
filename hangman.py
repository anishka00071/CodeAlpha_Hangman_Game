import random
import os
import time

# ------------------- ASCII ART -------------------
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

# ------------------- WORD BANK -------------------
WORDS = {
    "easy": ["apple", "chair", "bread", "river", "smile"],
    "medium": ["python", "laptop", "diamond", "monitor", "charger"],
    "hard": ["algorithm", "cryptography", "microprocessor", "sustainability"]
}

# ------------------- CLEAR SCREEN -------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ------------------- GAME LOGIC -------------------
def choose_word(level):
    return random.choice(WORDS[level])

def display_game(missed_letters, correct_letters, secret_word):
    clear_screen()
    print(HANGMAN_PICS[len(missed_letters)])
    print("\nMissed Letters:", " ".join(missed_letters))

    blanks = ""
    for letter in secret_word:
        if letter in correct_letters:
            blanks += letter + " "
        else:
            blanks += "_ "
    print("\nWord:", blanks)

def get_guess(already_guessed):
    while True:
        guess = input("\nGuess a letter: ").lower()
        if len(guess) != 1:
            print("❌ Enter only one letter.")
        elif not guess.isalpha():
            print("❌ Enter a valid alphabet.")
        elif guess in already_guessed:
            print("❌ You already guessed that letter.")
        else:
            return guess

def show_hint(secret_word, correct_letters):
    for letter in secret_word:
        if letter not in correct_letters:
            return letter
    return None

# ------------------- MAIN GAME -------------------
def play_game():
    clear_screen()
    print("🎮 WELCOME TO HANGMAN GAME 🎮")
    print("----------------------------------")
    print("Choose Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == "1":
            level = "easy"
            break
        elif choice == "2":
            level = "medium"
            break
        elif choice == "3":
            level = "hard"
            break
        else:
            print("❌ Invalid choice.")

    secret_word = choose_word(level)
    missed_letters = []
    correct_letters = []
    hints = 2
    score = 0

    while True:
        display_game(missed_letters, correct_letters, secret_word)

        print(f"\n💡 Hints left: {hints}")
        print(f"⭐ Score: {score}")

        guess = input("\nType a letter or type 'hint': ").lower()

        if guess == "hint":
            if hints > 0:
                hint_letter = show_hint(secret_word, correct_letters)
                if hint_letter:
                    correct_letters.append(hint_letter)
                    hints -= 1
                    print(f"Hint used! Letter revealed: {hint_letter}")
                    time.sleep(1)
                else:
                    print("No hints available!")
            else:
                print("❌ No hints left!")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input.")
            time.sleep(1)
            continue

        if guess in secret_word:
            correct_letters.append(guess)
            score += 10
        else:
            missed_letters.append(guess)
            score -= 5

        # WIN CONDITION
        if all(letter in correct_letters for letter in secret_word):
            clear_screen()
            print(f"🎉 YOU WON! 🎉")
            print(f"The word was: {secret_word}")
            print(f"🏆 Final Score: {score}")
            break

        # LOSE CONDITION
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_game(missed_letters, correct_letters, secret_word)
            print("\n💀 YOU LOST!")
            print(f"The word was: {secret_word}")
            print(f"🏆 Final Score: {score}")
            break

    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay == "yes":
        play_game()
    else:
        print("\nThanks for playing! 👋")

# ------------------- RUN GAME -------------------
if __name__ == "__main__":
    play_game()
