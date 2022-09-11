"""
Module which runs the game.
"""

# Imported for random integer generation
import random
# Imported to hold dictionaries of strings and one function to access them
import game

# Global constant list of winning cargo items in order
WINNING_CARGO = ['Eclipse Shield Cygnus', 'Anti-Gravity Device',
                 'Galaxy Transform', 'Tianzhou Device', 'SpaceX Mines']


def quit_out():
    """
    Quits application.
    Thank the player for playing and
    then quits the application.
    Parameters: No parameters.
    Returns: No return values.
    """
    print('\nThanks for playing Enter The Void!')
    quit()


def validate_start_menu_option():
    """
    Validates player choice at start menu.
    Asks the player what they want to do
    at the start menu and then
    validates whether the player wants to
    play Enter The Void, see the instructions for
    playing or quit the game.
    Parameters: No parameters.
    Returns: String which represents a number of 1, 2 or 3.
    """
    while True:
        print('\nWelcome to Enter The Void!\n')
        print('1) Play Enter The Void')
        print('2) Instructions for Enter The Void')
        print('3) Quit Enter The Void')
        number = (input('\nChoose which option you want by typing the '
                  'corresponding number.\n'))
        if number not in ['1', '2', '3']:
            print('Invalid choice option. Please input a number between 1 and '
                  '3.')
        else:
            return number


def main():
    """
    Sends the player where they want to go.
    Calls the start screen and receives the players
    input then sends them where they want to go.
    Parameters: No parameters.
    Returns: No return values, but does call other functions.
    """
    while True:
        option = validate_start_menu_option()

        if option == '1':
            introduction()
        elif option == '2':
            instructions()
        elif option == '3':
            quit_out()


def instructions():
    """
    Gives the player instructions on how to play the game.
    Parameters: No parameters.
    Returns: No return values. Just prints strings.
    """
    print(game.OTHER_DICT['instruct'])


def introduction():
    """
    Introduction to the game.
    Introduces the user to the game if
    they have chosen to play and then sends the
    player to create their own Player instance.
    Parameters: No parameters.
    Returns: No return values. Just prints strings
    and then calls function for player to get started on creating
    their own Player instance.
    """
    print(game.OTHER_DICT['intro'])
    create_player()


def validate_initial_cargo_choices(potential_cargo):
    """
    Validates the initial cargo choices.
    Asks the player to input a number and checks and
    validates if that number for the cargo is available.
    If not it creates a while loop where the player is
    asked to provide a valid number.
    Makes sure there are no value or index errors.
    Parameters:
    potential_cargo (list of str): List of items the player
    can potentially still take.
    Returns:
    number (int): Integer which is used to index the potential
    cargo items list outside the function.
    """
    while True:
        try:
            number = int(input('\nChoose which item you want by typing in the '
                               'number:\n')) - 1
            if number not in range(0, len(potential_cargo)):
                print(f'Please choose options between 1 and '
                      f'{len(potential_cargo)}.')
            else:
                return number
        except ValueError:
            print('Please type your option as an available number.')
