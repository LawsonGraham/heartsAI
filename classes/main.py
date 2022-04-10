import game
from player import Player

games = game.Game(Player('laws'), Player('jackie'), Player('cal'), Player('nate'), passDirection = 'Left')

games.playGame()

#https://www.geeksforgeeks.org/q-learning-in-python/