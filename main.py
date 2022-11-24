from words import words
import random


def get_valid_word(words):
    # Generate a random word
    word = random.choice(words)
    # Get a word with no spaces or dashes
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def get_underscores(word):
    # Get the dashes based on word lenght
    return "_" * len(word)

def play(words):
    game_over = False
    # Define the user lives
    lives = 6
    # Define the word
    word = get_valid_word(words)
    # Define the dashes
    dashes = get_underscores(word)
    # Define the set of letters
    letters_set = set(word)
    # Define the list of guessed letters
    letters_guessed = []
    # Welcome message
    print("Welcome to hangman\n"
    + "You have to guess the word\n" 
    + f"You only have {lives} lives\n")
    print(f"The word is :{dashes}")
    while game_over is False:
        user_letter = input("Please, enter a letter: ").upper()
        for char in letters_set:
            if user_letter == char:
                found = True
                break
            else:
                found = False
        status = ""
        if found:
            # Add the letter to the list of guessed letters
            letters_guessed.append(user_letter)
            print("The letter you entered is in the word!")
            letters_set.remove(user_letter)
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += "_"
            print(status)
        else:
            print("The letter you entered is not in the word")
            lives -= 1
            print(f"You have {lives} lives left")
        if len(letters_set) == 0:
            game_over == True
            print(f"Congratulations, you won! the word was {word.upper()}")
            break
        if lives == 0:
            game_over == True
            print("Game over, you lose")
            break
    

play(words)