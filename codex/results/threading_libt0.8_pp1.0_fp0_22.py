import threading
threading.stack_size(2048*2048)

#initialize pygame
pygame.init()

#load image from disk
boardImg = pygame.image.load("board5.jpg")

#create board
board = pygame.display.set_mode((boardImg.get_width(),boardImg.get_height()))

#put image on board
board.blit(boardImg,(0,0))

#refresh display
pygame.display.flip()

#initialize variables
quit = False
xPos = 0
yPos = 0
#main loop
def main():
        global xPos, yPos, quit, board, boardImg
        while quit == False:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                quit = True
                        #check if mouse is clicked
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                #get coords of click and put a circle there
                                xPos, yPos = pygame.mouse.get
