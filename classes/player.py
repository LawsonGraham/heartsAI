from ast import operator
from importlib.util import set_loader


class Player(object):
    
    def __init__(self, name = 'Daddy', hand = [], currPts = 0, pts = 0):
        self._hand = hand
        self._currPts = currPts
        self._name = name
        #self._wonLastTrick = wonLastTrick

    def set_hand(self, hand):
        self._hand = hand
    
    def play(self, playerNum):
        print('Your Hand:')
        print(self._hand)
        print(range(len(self._hand)))
        cardChoice = None
        while cardChoice == None or cardChoice > len(self._hand) or cardChoice < 0:
            try:
                cardChoice = int (input("Select the number corresponding to the card you'd like to play: "))
                if cardChoice == None or (cardChoice > len(self._hand) or cardChoice < 0):
                    print('You must select a NUMBER in range as listed above')
            except:
                print('You must select a NUMBER in range as listed above')
        return self._hand.pop(cardChoice)

    ##def isLastTrickWinner(self):
        ##return self.wonLastTrick

    ##def wonTrick(self):
        ##self.wonLastTrick = True

    
