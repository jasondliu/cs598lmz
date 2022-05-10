import socket
import sys
import threading
import time

from . import config
from . import utils
from . import core
from . import game
from . import player
from . import server
from . import ui

def main():
    """Main entry point for the program."""
    # Create the game
    game.game = game.Game()

    # Create the user interface
    ui.ui = ui.UI()

    # Create the server
    server.server = server.Server()

    # Create the local player
    player.player = player.Player()

    # Create the core
    core.core = core.Core()

    # Start the game
    game.game.start()

    # Start the user interface
    ui.ui.start()

    # Start the server
    server.server.start()

    # Start the core
    core.core.start()

    # Start the local player
    player.player.start()

    # Wait for the user interface to end
    ui.ui.join()

    # Stop the local player
    player.player.stop()
