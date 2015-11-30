__author__ = 'Pedro'

class Dice:
    MIN_DICE_VALUE = 1
    MAX_DICE_VALUE = 6

    def __init__(self, generator):
        self.generator = generator

    def roll(self):
        return self.generator.randint(self.MIN_DICE_VALUE, self.MAX_DICE_VALUE)
