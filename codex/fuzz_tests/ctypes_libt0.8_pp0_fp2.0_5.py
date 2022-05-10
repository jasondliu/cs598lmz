import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
pygame.init()

screenWidth = 450
screenHeight = 450

win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Bloxorz")

imgDir = path.join(path.dirname(__file__),"img")
fontDir = path.join(path.dirname(__file__),"ttf")

head = pygame.image.load(path.join("img","head.png"))
head = pygame.transform.scale(head, (50,50))

body = pygame.image.load(path.join("img","body.png"))
body = pygame.transform.scale(body, (50,50))

block = pygame.image.load(path.join("img","block.png"))
block = pygame.transform.scale(block, (50,50))

white = (255,255,255)


class Player():
    def __init__(self,
