import socket
import threading
import sys
import time
import select

class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.score = 0
        self.isAlive = True
        self.isMoving = False
        self.isShooting = False
        self.direction = 0
        self.isInGame = False
        self.isReady = False
        self.isDead = False
        self.isNew = True
        self.isFrozen = False
        self.isWaiting = False
        self.isWaitingForGame = False
        self.isWaitingForReady = False

    def setName(self, name):
        self.name = name

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setScore(self, score):
        self.score = score

    def setIsAlive(self, isAlive):
        self.isAl
