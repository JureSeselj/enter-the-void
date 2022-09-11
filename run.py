"""
Module which runs the game.
"""

# Imported for random integer generation
import random
# Imported to hold dictionaries of strings and one function to access them
import game

# Global constant list of winning cargo items in order
WINNING_CARGO = ['Eclipse Shield Cygnus', 'Anti-Gravity Device',
                 'Galaxy Transformer', 'Tianzhou Device', 'SpaceX Dragon Mines']


def quit_out():
    """
    Quits application.
    Thank the player for playing and
    then quits the application.
    Parameters: No parameters.
    Returns: No return values.
    """
    print('\nThanks for playing Star Traveller!')
    quit()
