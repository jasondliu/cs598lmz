import select
import time
import tty
import termios


##########################################
#										 #
#				TRON GAME		 		 #
#										 #
##########################################

#Trons Game Zone
GameZone = np.zeros((30,100)) + 3

# create a class to manage the game
class TronGame():
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.sprites = []
        self.game_over = False
        self.time = 0

    def add_sprite(self, sprite):
        self.sprites.append(sprite)
    def remove_sprite(self, sprite):
        self.sprites.remove(sprite)
# create a class to manage the game
class TronGame():
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.sprites = []
        self.game_over = False
       
