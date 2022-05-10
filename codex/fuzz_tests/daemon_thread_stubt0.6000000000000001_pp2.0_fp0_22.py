import sys, threading

def run():
    """
    The main function that starts the game
    """
    pg.init()
    mixer.init()
    pg.display.set_caption("Bubble Trouble")
    # Loading the music and the sound effects
    mixer.music.load("music.wav")
    mixer.music.play(-1)
    # Create a list of sound objects
    sounds = [mixer.Sound("pop.wav"), mixer.Sound("death.wav"), mixer.Sound("win.wav")]
    # Load the images
    images = [pg.image.load(x) for x in ["player.png", "bubble.png", "background.png", "heart.png"]]
    # Create a list of bubble images
    bubble_img = [pg.transform.scale(images[1], (x, x)) for x in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]
    # Create a list of heart images
    heart_img = [pg.transform.scale(images[3], (x, x)) for x in [20, 25, 30, 35
