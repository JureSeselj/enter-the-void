"""
Module which runs the game.
"""

# Imported for random integer generation
import random
# Imported to hold dictionaries of strings and one function to access them
import game

# Global constant list of winning cargo items in order
WINNING_CARGO = ['Eclipse Shield Cygnus', 'Anti-Gravity Device',
                 'Galaxy Translator', 'Tianzhou Device', 'SpaceX Mines']


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


def validate_replay_choice():
    """
    Validates whether player wants to replay game.
    Validates whether the player has chosen either 'Y' or 'N'
    for their choice in the replay function. Creates
    while loop so player must input correctly.
    Parameters: No parameters.
    Returns:
    replay_choice(chr): 'Y' or 'N' so that player can
    replay or quit game.
    """
    while True:
        replay_choice = input('Type Y for yes and N for no:\n').upper()
        if replay_choice not in ['Y', 'N']:
            print('\nSorry, that choice is not available.')
        else:
            return replay_choice


def validate_scenario_choice(player_object):
    """
    Validates the player's scenario choice.
    Validates whether the player has inputted a
    possible scenario choice that is available to them.
    Creates while loop so that player must input
    a valid choice.
    Parameters:
    player_object (Player): Used to work out the length of the
    list of cargo items so that the player's input can be assessed
    against the list of available inputs.
    Returns:
    number (int): Returned so that the game can decide where to proceed.
    Whether the player has progressed to the next scenario, achieved victory
    or recieved a game over and what text is associated with that.
    """
    while True:
        try:
            number = int(input('\nPlease choose an option using the numbers '
                               'provided:\n'))
            if number not in range(1, len(player_object.cargo) + 3):
                print(f'Please choose options between 1 and '
                      f'{len(player_object.cargo) +2}.')
            else:
                return number
        except ValueError:
            print('Please type your option as an available number.')


def get_name(name_in_question):
    """
    Asks the player to name something in their Player instance.
    Asks the user's name for captain or ship
    depending on argument provided and validates
    whether that is correct by creating a while loop and checking
    that the name is valid.
    Parameters:
    name_in_question (str): Either the name of the player's
    captain or the spaceship's name.
    Returns:
    name (str): Returns a string which is used to develop the Player
    instance. If the argument is the spaceship name then a 'the '
    is added to the front of the string.
    """
    while True:
        name = ((input(f'\nWhat is your {name_in_question}, captain?\n'))
                .strip()).capitalize()
        if len(name) > 10 or len(name) < 4 or not name.isalnum():
            print(f'{name_in_question.capitalize()} must be between 4 and 10 '
                  'alphanumeric characters without spaces.')
        else:
            if name_in_question == 'ship name':
                name = 'the ' + name
            return name


def decide_on_items():
    """
    Asks the player to choose three items out of potential 5.
    Asks player to choose items and presents a shrinking list
    as they pick more. Appends a new list that is used for the
    Player instance.
    Parameters: No parameters.
    Returns:
    cargo (list of str): Returns cargo list which is used to
    instantiate the Player instance for the game.
    """
    print('\nOn your journey you will need to take some items for perilous '
          'situations.')
    potential_cargo_items = ['Eclipse Shield Cygnus', 'Anti-Gravity Device',
                             'Galaxy Translator', 'Tianzhou Device', 
                             'SpaceX Mines']
    cargo = []
    counter = 1
    while counter < 4:
        print('\nHere are the list of items you can still take:\n')
        for potential_cargo_item, i in zip(potential_cargo_items,
                                           range(len(potential_cargo_items))):
            print(f'{i + 1}) {potential_cargo_item}')
        cargo_choice = validate_initial_cargo_choices(potential_cargo_items)
        cargo.append(potential_cargo_items[cargo_choice])
        potential_cargo_items.remove(potential_cargo_items[cargo_choice])
        counter += 1

    return cargo


def scenario_conclusion(player_object, scenario, conclusion_number):
    """
    Function which acts as 'switch' to retrieve conclusion text.
    Parameters:
    player_object (Player): Instance of Player class
    created by player at start of game.
    scenario (int): Integer to identify which scenario is taking
    place currently in the game.
    conclusion_number (int): Integer to identify which conclusion
    has happened based on game logic.
    Returns: Returns nothing.
    """
    print('\n')
    if scenario == 1:
        if conclusion_number == 1:
            game.retrieve_scenario_text(player_object, 1, 1)
        elif conclusion_number == 2:
            raise IndexError('This shouldn\'t be possible in the first '
                             'scenario as the player\'s fuel can\'t decrease '
                             'this low in the first scenario.')
        elif conclusion_number == 3:
            game.retrieve_scenario_text(player_object, 1, 3)
        elif conclusion_number == 4:
            game.retrieve_scenario_text(player_object, 1, 4)
        elif conclusion_number == 5:
            game.retrieve_scenario_text(player_object, 1, 5)
    elif scenario == 2:
        if conclusion_number == 1:
            game.retrieve_scenario_text(player_object, 2, 1)
        elif conclusion_number == 2:
            raise IndexError('This shouldn\'t be possible in the first '
                             'scenario as the player\'s fuel can\'t decrease '
                             'this lowin the second scenario.')
        elif conclusion_number == 3:
            game.retrieve_scenario_text(player_object, 2, 3)
        elif conclusion_number == 4:
            game.retrieve_scenario_text(player_object, 2, 4)
        elif conclusion_number == 5:
            game.retrieve_scenario_text(player_object, 2, 5)
    elif scenario == 3:
        if conclusion_number == 1:
            game.retrieve_scenario_text(player_object, 3, 1)
        elif conclusion_number == 2:
            game.retrieve_scenario_text(player_object, 3, 2)
        elif conclusion_number == 3:
            game.retrieve_scenario_text(player_object, 3, 3)
        elif conclusion_number == 4:
            game.retrieve_scenario_text(player_object, 3, 4)
        elif conclusion_number == 5:
            game.retrieve_scenario_text(player_object, 3, 5)
    elif scenario == 4:
        if conclusion_number == 1:
            game.retrieve_scenario_text(player_object, 4, 1)
        elif conclusion_number == 2:
            game.retrieve_scenario_text(player_object, 4, 2)
        elif conclusion_number == 3:
            game.retrieve_scenario_text(player_object, 4, 3)
        elif conclusion_number == 4:
            game.retrieve_scenario_text(player_object, 4, 4)
        elif conclusion_number == 5:
            game.retrieve_scenario_text(player_object, 4, 5)
    elif scenario == 5:
        if conclusion_number == 1:
            game.retrieve_scenario_text(player_object, 5, 1)
        elif conclusion_number == 2:
            game.retrieve_scenario_text(player_object, 5, 2)
        elif conclusion_number == 3:
            game.retrieve_scenario_text(player_object, 5, 3)
        elif conclusion_number == 4:
            game.retrieve_scenario_text(player_object, 5, 4)
        elif conclusion_number == 5:
            game.retrieve_scenario_text(player_object, 5, 5)
    return


def replay():
    """
    Function which acts as 'switch' for replaying the game.
    This function calls the validation function for
    the player's replay choice and then calls a function to
    go to the start menu or quit the game (and terminal)
    entirely.
    Parameters: No parameters.
    Returns: Returns nothing.
    """
    print('Would you like to play again?')
    choice = validate_replay_choice()
    if choice == 'Y':
        main()
    elif choice == 'N':
        quit_out()


def game_over(player_object):
    """
    Function which is called when the player loses the game.
    Prints game over text and allows them to
    quit or play again by calling
    replay function.
    Parameters:
    player_object (Player): Uses this to print an fstring
    with the name of the captain inside.
    Returns: Returns nothing.
    """
    print(f'\n\nCaptain {player_object.name} has died.')
    replay()
