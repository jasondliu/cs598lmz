import sys, threading

def run():
    """
    Run the main loop
    """
    #try:
    #    import psyco
    #    psyco.full()
    #except ImportError:
    #    pass

    # Initialize the game
    pygame.init()

    # Initialize the game's sound engine
    sound.init()

    # Create the main game window
    screen = pygame.display.set_mode(config.screen_size)
    pygame.display.set_caption(config.game_name)

    # Create a clock to limit framerate
    clock = pygame.time.Clock()

    # Create the player
    player = Player(screen, config.player_image, config.player_speed, config.player_health, config.player_lives, config.player_start_x, config.player_start_y, config.player_respawn_x, config.player_respawn_y)
    player.draw()

    # Create the enemies
    enemies = []
    for x in range(config.enemy_start_x, config.enemy_start_x + (config
