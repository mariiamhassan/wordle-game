import random
from colorama import Fore, Style, init

init(autoreset=True)

def load_words(file_path):
    with open(file_path) as f:
        return [word.strip().lower() for word in f if len(word.strip()) == 5]

def check_guess(guess, secret):
    result = ""
    for i in range(5):
        if guess[i] == secret[i]:
            result += Fore.GREEN + guess[i].upper()
        elif guess[i] in secret:
            result += Fore.YELLOW + guess[i].upper()
        else:
            result += Fore.WHITE + guess[i].upper()
        
        if i < 4: 
            result += " | "
    return result

def wordle_game(guesses, answers):
    print("🎮 Welcome to Wordle! Try to guess the 5-letter word. You have 6 tries.")
    secret_word = random.choice(answers)

    tries = 0
    while tries < 6:
        guess = input(f"\nTry {tries + 1}/6: ").lower()

        if guess not in guesses or len(guess) != 5:
            print(Fore.RED + "❗ Invalid guess. Make sure it's a real 5-letter word.")
            continue

        if guess == secret_word:
            print(Fore.GREEN + "\n🎉 You got it! The word was: " + secret_word.upper())
            return

        print(check_guess(guess, secret_word))
        tries += 1

    print(Fore.RED + "\n💥 Game Over! The correct word was: " + secret_word.upper())

guesses = load_words("guesses.txt")
answers = load_words("answers.txt")

wordle_game(guesses, answers)

