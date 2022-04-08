import random
from card import Card

class Deck(object):
    def __init__(self, deck = []):
        self.suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.deck = deck

    def shuffleMe(self):
        if len(self.deck) == 0:
            for suit in self.suits:
                for i in range(2,15):
                    self.deck += [Card(i, suit)]
            random.shuffle(self.deck)
        return self.deck



