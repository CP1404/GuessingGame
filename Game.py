"""
Game - represents the state of game-play of our guessing game
"""


# TODO make the field 'secret' a random value in the range 1 - 10

# TODO implement guess() - it should compare the given value with the secret
# TODO guess() returns 'found it', 'try bigger', 'try smaller'

# TODO add a number_of_moves counter


from random import randint


class Game:
    def __init__(self):
        self.secret = 0

    def guess(self, value):
        pass
