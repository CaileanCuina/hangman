# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import randint
import numpy as np


def print_welcome(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}. We will start with a nice word for you.')  # Press Strg+F8 to toggle the breakpoint.


def read_words(mode):
    file_name = mode + "_words.txt"
    with open(file_name, 'r') as file:
        content = file.read()
    return content.split(',')


def fetch_random_word(word_list: list, already_used: list) -> str:
    chosen_word: str = word_list[randint(0, len(word_list) - 1)]
    while chosen_word in already_used:
        chosen_word = word_list[randint(0, len(word_list) - 1)]
    return chosen_word


def guess_letter(result: list, users_guess: list) -> int:
    guess: str = input("Please enter your guess?")
    if guess.upper() in result:
        modify_result_labels(result, users_guess, guess)
        return 0
    return 1


def modify_result_labels(old: list, new: list, word: str):
    idx = old.index(word)
    new[idx] = word
    old[idx] = '_'



def print_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        --------
        """,
    ]
    print(stages[tries])


def start_game(word: str):
    result = list(word)
    users_guess = ['_'] * (len(word))
    print('The word is chosen, here are the blanks.')
    print(users_guess)
    num_miss_guess = 0
    while result.count('_') != len(result):
        num_miss_guess = num_miss_guess + guess_letter(result, users_guess)
        if num_miss_guess > 6:
            print('Oh no. You died.')
            return
        print_hangman(num_miss_guess)
        print(f'your result: {users_guess}')
    print('Congratulations! You won.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to Hangman lets start hangin em all!')
    name = input("Whats your name?")
    print_welcome(name)
    start_game(fetch_random_word(read_words("easy"), []))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
