from card import Card


class GameState(object):
    def __init__(self, players, points = 0, cardsPlayed = [], movesLeft = 52, lastState = None, order = None, currentTrick = [None, None, None, None], currentPlayerTurn=0):
        self._players = players # instance of player
        self._points = points # total points played (hearts and queen of spades)
        self._cardsPlayed = cardsPlayed # array of all cards played
        self._movesLeft = movesLeft # moves until end
        self._lastState = lastState # last GameState
        self._order = order # order of who plays
        if order == None: # start of game must have the player with the 2 of clubs begin
            start = Card(2, 'Clubs')
            for i in range(4):
                if start in self._players[i]._hand: ## contains probably doesnt work
                    self._order = self._players[i:] + self._players[:i]
                    break
        self._currentTrick = currentTrick
        self._currentPlayerTurn = currentPlayerTurn
    def getPlayer(self, num):
        return self._players[num]


    
