from ast import operator
from random import shuffle
from types import NoneType
from player import Player
from deck import Deck
from gamestate import GameState
from card import Card

class Game(object):
    def __init__(self, player1, player2, player3, player4, gamestate=None):
        if gamestate == None:
            shuffledDeck = Deck().shuffleMe()
            self._players = [player1.recieveHand(shuffledDeck[0:13]), player2.recieveHand(shuffledDeck[13:26]), player3.recieveHand(shuffledDeck[26:39]), player4.recieveHand(shuffledDeck[39:52])] # array of players
            self._gamestate = GameState(self._players)
            print (self._gamestate._order)
        else:
            for i in range (0,4):
                self._players.append(gamestate.getPlayer(i))
            self._gamestate = gamestate

    def playGame(self):
        while self._gamestate._movesLeft >= 0:
            print (self._gamestate._movesLeft)
            # check if we need to clear the trick
            if self._gamestate._currentTrick[3] is not None: 
                winningPlayer = self.findWinner(self._gamestate._currentTrick, self._gamestate._order) #winningPlayer = Player object
                newPoints = 0
                for card in self._gamestate._currentTrick:
                    if card.suit() == 'Hearts':
                        winningPlayer._currPts += 1
                        newPoints += 1
                    if card == Card(12, 'Spades'):
                        winningPlayer._currPts += 13
                        newPoints += 13

                for i in range(4):
                    if winningPlayer == self._players[i]:
                        winningPlayerIndex = i
                self._gamestate = GameState(self._players, self._gamestate._points + newPoints, self._gamestate._cardsPlayed, self._gamestate._movesLeft, self._gamestate, self._players[winningPlayerIndex:] + self._players[:winningPlayerIndex], currentTrick=[None, None, None, None])
            ## TURN LOGIC
            if self._gamestate._movesLeft != 0:
                currPlayer = self._gamestate._currentPlayerTurn
                self.printState()
                if self._gamestate._movesLeft == 52:
                    self._gamestate._order[currPlayer]._hand.remove(Card(2, 'Clubs'))
                    cardSelected = Card(2, 'Clubs')
                else:
                    cardSelected = self._gamestate._order[currPlayer].play(currPlayer, self._gamestate._currentTrick[0])

                self._gamestate._cardsPlayed.append(cardSelected)
                self._gamestate._currentTrick[currPlayer] = cardSelected
            ## UPDATE GAMESTATE
            self._gamestate = GameState(self._players, self._gamestate._points, self._gamestate._cardsPlayed, self._gamestate._movesLeft - 1, self._gamestate, self._gamestate._order, self._gamestate._currentTrick, self._gamestate._currentPlayerTurn + 1)
                
    
        print (self._gamestate._points)
        print (self._gamestate._movesLeft)
        print (self._gamestate._lastState._points)
        print (len(self._gamestate._cardsPlayed))
        print (self._gamestate._cardsPlayed)

        for i in range(len(self._gamestate._cardsPlayed)):
            if self._gamestate._cardsPlayed[i] == Card(2, 'Clubs'):
                print ('dub')
        for i in range(4):
            print (self._players[i]._name, self._players[i]._currPts)
        for i in range(4):
            if self._players[i]._currPts == 26:
                for h in range(4):
                    self._players[h]._currPts = 26
                self._players[i]._currPts = 0
                break

        
    def findWinner(self, finishedTrick, playerOrder):
        ledSuit = finishedTrick[0].suit()
        print(finishedTrick)
        print (playerOrder)
        helperList = [[finishedTrick[i], playerOrder[i]] for i in range(4)]
        currentWinner = playerOrder[0]
        currentMax = 0
        for i in range(1, 4):
            if helperList[i][0].value() > currentMax and helperList[i][0].suit() == ledSuit:
                currentWinner = helperList[i][1]
                currentMax = helperList[i][0].value()
        return currentWinner

    def printState(self):
        print ('Current Trick:')
        print (self._gamestate._currentTrick)
        print ('Player scores: ')
        for player in self._gamestate._players:
            print (str(player) + ": " + str(player._currPts) + " ")