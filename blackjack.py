# Distribute 2 cards to player, 2 to dealer.
# See only the 1st card that the dealer received.
# Ace can be worth 1 or 11.
# If you have 21, you win
# If dealer has 21, he wins
# If both have 21, it's a draw.
# Player decided whether to draw another card, until you bust or stop.
# Dealer must draw as long as he has below 17.
# Then ask for replay, and clear console.
#
import random
from dataclasses import dataclass
deck = {str(i):i for i in range(2,10+1)}
deck.update({'J':10, 'Q':10, 'K':10, 'A':-1})
deck

@dataclass
class Hand:
    cards: list
    total: int = 0 # total of all cards except Aces
    num_aces: int = 0 # number of aces, that each may take the value of 1 or 10

    def __init__(self):
        self.cards = []
        self.total = 0

    def draw(self, cheat=None):
        """
            Args:
                cheat: if specified, don't draw at random, draw `cheat` card instead.

        """
        if cheat is not None:
            card = cheat
        else:
            card = random.sample(list(deck), 1)[0] # returns 1 string, e.g. 'Q'

        value = deck[card]
        if value == -1:
            self.num_aces += 1
        else:
            self.total += value
        self.cards += [card]
        return card

# Unit test 1
ph = Hand()
ph.draw('A')
assert ph.cards == ['A']
assert ph.total == 0
assert ph.num_aces == 1
ph.draw('2')
assert ph.cards == ['A', '2']
assert ph.total == 2
assert ph.num_aces == 1

ph.draw()
ph




ph = Hand()
for i in range(2):
    ph.draw()
ph.cards
ph

dh = Hand()
for i in range(2):
    dh.draw()
dh.cards
