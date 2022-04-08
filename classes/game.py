from ast import operator
from random import shuffle
from types import NoneType
from player import Player
from deck import Deck
from gamestate import GameState
from card import Card

class Game(object):
    def __init__(self, player1name, player2name, player3name, player4name, gamestate=None):
        if gamestate == None:
            shuffledDeck = Deck().shuffleMe()
            self._players = [Player(player1name, shuffledDeck[0:13]), Player(player2name, shuffledDeck[13:26]), Player(player3name, shuffledDeck[26:39]), Player(player4name, shuffledDeck[39:52])] # array of players
            self._gamestate = GameState(self._players)
        else:
            for i in range (0,4):
                self._players.append(gamestate.getPlayer(i))
            self._gamestate = gamestate

    def playGame(self):
        while self._gamestate != 0:
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
                print(self._gamestate._currentTrick)
                self._gamestate = GameState(self._players, self._gamestate._points + newPoints, self._gamestate._cardsPlayed + self._gamestate._currentTrick, self._gamestate._movesLeft, self._gamestate, self._players[winningPlayerIndex:] + self._players[:winningPlayerIndex], currentTrick=[None, None, None, None])
                print(self._gamestate._currentTrick)
            ## TURN LOGIC
            currPlayer = self._gamestate._currentPlayerTurn
            self.printState()
            cardSelected = self._gamestate.getPlayer(currPlayer).play(currPlayer)
            ## UPDATE GAMESTATE
            self._gamestate = GameState(self._players, self._gamestate._points, self._gamestate._cardsPlayed, self._gamestate._movesLeft - 1, self._gamestate, self._gamestate._order, self._gamestate._currentTrick, self._gamestate._currentPlayerTurn + 1)
            self._gamestate._cardsPlayed.append(cardSelected)
            self._gamestate._currentTrick[currPlayer] = cardSelected

        
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