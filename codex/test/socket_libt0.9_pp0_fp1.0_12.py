import socket
import sys
from thread import *
from collections import deque
from ledStrip import *
from Motor import *
#from search import *

from player import Player
from monster import Monster
from environment import Environment


def threaded_client(conn):
	envi = Environment()
	player = Player()
	monster = Monster()
	startStrip()


	def inputChecker():
		while not player.stop:
			if len(player.input):
				player.input = deque(maxlen = 5)
		player.stop = True
		return

	def monsterChecker():
		while not monster.stop:
			monster.Move(player.position)
			time.sleep(0.5)
		monster.stop = True
		return

