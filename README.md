# Enter The Void

[Here is the live version of Enter The Void]()
## Purpose of Enter The Void

Enter The Void is a text-based adventure game in a science fiction setting. The game receives input from the user and through this the user navigates through a number of scenarios, either passing them and moving on to the next one or failing. There are five scenarios the player must navigate through by inputting commands and completing all five of them will result in the user completing the game. The user will choose the name of their captain, their spaceship and will decide upon 3 of 5 'cargo' to hold on their ship to potentially use throughout the game.

The game is simple, but is designed for people who would enjoy science fiction. The games primary enjoyment comes from passing the scenarios and reading the conclusions and also from its replayability, with 23 possible different scenario conclusions that the player can receive.

## Features

* Start Menu
    * The player is taken to a start menu to begin with. Here they are prompted to choose between numbers 1-3 with details next to the numbers. 
    * If the player inputs 1 they are taken to the introduction text of the game and then to create their player object.
    * If the player inputs 2 they are taken to the instructions text and then back to the start menu.
    * If the player inputs 3 they exit the application.
    * If they input an invalid repsonse they are asked to input a valid response.

* Create Player
    * The player is asked to name their captain and their ship. The names must be between 4 and 15 alphanumeric characters without spaces and if they aren't the player is prompted to do this.
    * They are asked if these names are correct and if not this happens again in a loop but if so moves on to the player choosing what cargo they want. The player confirms their choice by responding by inputting 'Y' or 'N'. 
    * They are then asked to choose from five pieces of cargo with number inputs. The cargo list shrinks when taken from and choosing a non integer causes the game to ask the player to type an available number and typing an out of index number causes the game to tell the player what number range is available.
    * The player is asked if the cargo is good when they have selected three pieces and if the player decides they aren't the process starts again but if they are the player object is created using the captain name, ship name and the cargo chosen. The player object also has two methods which allow it to use fuel and take a chance in a scenario.  

* Scenario 
    * The player is then taken to the scenario where they are given an introductory message and are given the options of what they can do in available numbers. 
    * Choosing an incorrect option will ask the player to type an integer if they create an index error or will give the range of integers available if the players input is outside of index bounds.
    * Other than using available cargo items, the player can burn fuel (starts at 2 and decreases after every use) and take a risk with the two class methods of the player class.
    * Using the correct cargo item for the scenario clears the scenario but using the wrong one will fail it. It will also remove the cargo item from the players options.
    * Burning fuel automatically passes the scenario but if fuel is 0 or below will fail the scenario. Burning fuel also reduces fuel amount by 1 each time.
    * Taking a chance returns a random integer between 1 and 10. If the player scores higher than the scenario's 'risk factor' then they succeed otherwise they fail. Each scenario increases the risk factor by 2; so scenario 1 is a 1 and always winnable but scenario 5 is a 9 and very risky for the player.
    * Succeeding in a scenario takes you to the next scenario or victory if all scenarios are complete but failing takes you to the game over.

* Victory and Game Over
    * Whether the player achieves victory or gets a game over, they will be asked if they want to replay the game. 
    * If they choose no they will exit the application.
    * If they choose yes they will be taken back to the start menu.
    * If they choose an option that is not 'Y' or 'N' they will be asked to provide an answer that is either 'Y' or 'N' (lowercases are capitalised).