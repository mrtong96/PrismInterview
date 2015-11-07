
### Overview ###

This is the README file for the Prism interview. In here you can find the descriptions for cards.py and vacationing_salesman.py

### Cards.py ###

* To run a demo of this file, run the following command:

```
$ python cards.py
```

* The two objects: Deck and Card, represent the deck and cards
* API for Deck:
	* init, creates a new deck using NewDeck()
	* Shuffle, creates a new deck with all of the cards in a random order.
	* NewDeck, creates a new deck in the order of A-2, then hearts, clubs, diamonds, spades.
	* GetNextCard, deals the next card if it exists, otherwise throws an exception
* API for Card
	* init, create a card with an arbitrary suit (str) and value (str)
	* str, repr, get the string representation of the object in the form '< value > of < suit >'
* For testing the correctness of this module, would write unit tests. See test_cards.py for an example.

### Vacationing Salesman.py ###

* Designed to be used in the form of 'python vacationing_salesman.py < < input file >' where < input file > is a text file. Example below:

```
$ python vacationing_salesman.py < example_input.txt
```

* Each line in the input file can contain either whitespace, a flag, or a destination.
* Only one destination can be listed.
* For more details about the flags, place the line '--help' in the first line of your input file and run this program.
* Writes the output to stdout.
* This is written in python because I am most comfortable in python.
* The idea behind writing the flags was to make this easy to parse, while mimicking the unix style for familiarity.
* The reason why I didn't make everything on one line was for easier readability of the commands and flags.

### Contact ###

github: mrtong96
email: mrtong96@berkeley.edu

### Other Interesting Projects ###

* mazeSolver: program that can solve images of mazes and overlay the solution on the original image.
* RPS: bot that uses combination of Monte Carlo and MDP to exploit non-randomness in humans in the game 'Rock, Paper, Scissors'

