import _struct

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHTRED = (255, 0, 0)
GREEN = (34, 177, 76)
LIGHTGREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 255, 255)
GREY = (50, 50, 50)
SCORE_COLOUR = (37, 49, 66)

#display
game_display = pygame.display.set_mode((800,600))
pygame.display.set_caption('TicTacToe')

#board
board = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
