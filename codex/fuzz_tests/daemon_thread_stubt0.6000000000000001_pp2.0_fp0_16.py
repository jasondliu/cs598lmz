import sys, threading

def run():
    """
    Run the main loop.
    """
    global running
    running = True
    
    # Initialize the agent
    agent = Agent(config.AGENT_CONFIG)
    
    # Initialize the game
    game = Game(config.GAME_CONFIG, agent, config.GAME_PARAMS)
    
    # Initialize the renderer
    renderer = Renderer(config.RENDERER_CONFIG, game)
    
    # Start the game loop
    while running and game.running:
        game.update()
        renderer.update()
        time.sleep(config.GAME_LOOP_DELAY)

def main():
    """
    Main entry point.
    """
    # Create the main thread
    mainThread = threading.Thread(target=run, args=())
    
    # Start the main thread
    mainThread.start()
    
    # Wait for the main thread to finish
    mainThread.join()

if __name__ == "__main__":
    main()
