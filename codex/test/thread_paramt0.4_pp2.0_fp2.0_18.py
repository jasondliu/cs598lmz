import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Initialize the game
game = Game(2)

# Define a player
def my_agent(observation, configuration):
    from random import choice
    return choice([c for c in range(configuration.columns) if observation.board[c] == 0])

# Run the game
game.run(my_agent)

# Print the result
print(game.result)

# Print the board
print(game.board)
