import selectors
import socket
import time
import random

#TO DO:
#Add more questions - create question database
#Logic to make it impossible to guess the same answer twice, to avoid guessing the same answer twice in a row (ie. if someone is a cheater)
#Remove the options that have already been played/guessed
#Make a database that stores multiple questions instead of only one
#Also add logic for the server to restart the game when the player quits with a full game, to avoid players from being stuck at "waiting for partner to connect"

host = '127.0.0.1'
port = 65432

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.score = 0
        self.guess = ""
        self.connection = []

    def draw(self,win):
        pygame.draw.rect
