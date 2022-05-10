import ctypes
ctypes.windll.kernel32.SetConsoleTitleW(Title)

#Initialize the pygame engine
pygame.init()

#Initialize the mixer
pygame.mixer.init()

#Create the window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(Title)

#Initialize the clock
clock = pygame.time.Clock()

#Import the music
pygame.mixer.music.load(r"C:\Users\Nathan\Desktop\Python\Pygame\Game\Music\MainTheme.mp3")
pygame.mixer.music.play(-1)

#Import the images
background = pygame.image.load(r"C:\Users\Nathan\Desktop\Python\Pygame\Game\Background\Background.png")

#Import the player
playerImg = pygame.image.load(r"C:\Users\Nathan\Desktop\Python\Pygame\Game\Sprites\Player.png")
playerX = WIDTH/2
playerY = HEIGHT/2
