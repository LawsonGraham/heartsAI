from ast import operator
from importlib.util import set_loader


class Player(object):
    
    def __init__(self, name = 'Daddy', hand = [], currPts = 0, pts = 0):
        self._currPts = currPts
        self._name = name  
        self._hand = []
        self._lifetimePts = pts

        #self._wonLastTrick = wonLastTrick

    def set_hand(self, hand):
        self._hand = hand
    
    def play(self, playerNum, leadCard):
        print(f'Your Hand ({self._name}):')
        print(self._hand)
        cardChoice = None
        while cardChoice == None or cardChoice > len(self._hand) or cardChoice < 0:
            try:
                cardChoice = int (input("Select the index corresponding to the card you'd like to play: "))
                if cardChoice == None or (cardChoice >= len(self._hand) or cardChoice < 0):
                    print('You must select a NUMBER in range as listed above')
                    cardChoice = None
                if leadCard != None:
                    if self._hand[cardChoice].suit() != leadCard.suit() and self.hasSuit(leadCard.suit()):
                        print (f'You have {leadCard.suit()} in positions {self.findSuits(leadCard.suit())}, you cannot play offsuit.')
                        cardChoice = None
            except:
                print('You must select a NUMBER in range as listed above')
        return self._hand.pop(cardChoice)


    def __str__(self):
     return str(self._name)

    def __repr__(self):
        return str(self._name)

    ##def isLastTrickWinner(self):
        ##return self.wonLastTrick

    ##def wonTrick(self):
        ##self.wonLastTrick = True

    def hasSuit(self, suit):
        return any([card.suit() == suit for card in self._hand])

    def findSuits(self, suit):
        return [ind for ind, card in enumerate(self._hand) if card.suit() == suit]

    def recieveHand(self, hand):
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            suits = [card for card in hand if card.suit() == suit]
            if suits != []:
                suits.sort(key = lambda card: card.value())
                self._hand += suits
        return self

    
    def pass3(self):
        cards = []
        cardsIndexSelected = []
        count = 1
        while len(cards) != 3:
            try:
                cardChoice = int (input(f'Card {count}:'))
                if cardChoice not in cardsIndexSelected and not (cardChoice >= len(self._hand) or cardChoice < 0):
                    cards += [self._hand[cardChoice]]
                    cardsIndexSelected +=[cardChoice]
                    count += 1
                else:
                    print('You must select a NUMBER in range as listed above that has not been selected')
            except:
                print('You must select a NUMBER in range as listed above')
        
        for card in cards:
            self._hand.remove(card)
        return cards

    def organizeCards(self):
        newHand = []
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            suits = [card for card in self._hand if card.suit() == suit]
            if suits != []:
                suits.sort(key = lambda card: card.value())
                newHand += suits
        self._hand = newHand
        return self