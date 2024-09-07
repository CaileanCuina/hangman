import time
from random import randint
import PySimpleGUI as sg
from PySimpleGUI import Window


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


def guess_letter(result: list, users_guess: list, guess: str) -> int:
    if guess.upper() not in result:
        return 1
    while guess.upper() in result:
        modify_result_labels(result, users_guess, guess.upper())
    return 0


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
    return stages[tries]


def start_game(word: str, name: str) -> str:
    users_guess = ['_'] * (len(word))
    result = list(word)
    num_miss_guess = 0
    hangman_result = print_hangman(num_miss_guess)
    layout = [[sg.Text('Hi ' + name + '. The word is chosen, here are the blanks.')],
              [sg.Text('Enter a Letter.')], [sg.Text(users_guess, key="guess")],
              [sg.InputText(do_not_clear=False)],
              [sg.Text(hangman_result, key="hangman")],
              [sg.Button('Confirm'), sg.Button('Cancel')]]
    window = sg.Window('Hangman', layout)

    while True:
        event, values = window.read()
        if event == 'Confirm':
            if len(values[0]) == 1:
                num_miss_guess = num_miss_guess + guess_letter(result, users_guess, values[0])
                if num_miss_guess > 6:
                    print('Oh no. You died.')
                    window.close()
                    return "fail"
                window['hangman'].update(print_hangman(num_miss_guess))
                window['guess'].update(users_guess)
                window.refresh()
            else:
                sg.popup_quick_message("Only one Letter allowed.")
        if result.count('_') == len(result):
            sg.popup_ok('Congratulations! You won.')
            break
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
    window.close()
    return word


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    already_used_words = []
    layout = [[sg.Text('Welcome to Hangman lets start hangin em all!')],
              [sg.Text("What's your name?")],
              [sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Hangman', layout)
    name = ''
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Ok':
            name = values[0]
            window.close()
            window = sg.Window('Hangman', [[sg.Text('Going for a round?')],
                                           [sg.Button('Start'), sg.Button('Cancel')]])

        if event == 'Start':
            window.close()
            already_used_words.append(
                start_game(fetch_random_word(read_words("easy"), already_used_words).upper(), name))
            window = sg.Window('Hangman', [[sg.Text('Going for a round?')],
                                           [sg.Button('Start'), sg.Button('Cancel')]])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
