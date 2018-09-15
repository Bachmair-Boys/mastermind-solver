from Guess import Guess
from Colors import Colors as c

guess1 = Guess([c.Y, c.G, c.R, c.Bk],0,2)
guess2 = Guess([c.Bk, c.W, c.Y, c.Bu],1,1)
guess3 = Guess([c.G, c.Bu, c.W, c.R],1,1)
guess4 = Guess([c.W, c.R, c.Bk, c.R],0,1)
guess5 = Guess([c.R, c.R, c.G, c.G],1,1)
guesses = [guess1,guess2,guess3,guess4,guess5]
explanations = []
colors = [c.Y,c.G,c.R,c.Bk,c.Bu,c.W]
possibilities = [colors] * 4


def apply_rule1():
    for guess in guesses:
        if guess.num_blacks == 0:
            for color in guess.sequence:
                for possibility in possibilities:
                    if color in possibility:
                        possibility[possibility.index(color)] = c.NONE


def print_possibilities():
    for p in possibilities:
        print(p)

apply_rule1()
print_possibilities()


