import threading
threading.stack_size(67108864)

def main():
    # Initialize the game engine
    pygame.init()

    # Define the colors we will use in RGB format
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Set the height and width of the screen
    size = [800, 600]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Example code for the draw module")

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QU
