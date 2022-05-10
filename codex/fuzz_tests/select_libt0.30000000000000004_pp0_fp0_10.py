import select
import sys
import time
import traceback
import tty
import termios


class Terminal:
    """
    A class for controlling the terminal.
    """

    def __init__(self):
        """
        Initialize the terminal.
        """

        # Save the original terminal settings.
        self.original_settings = termios.tcgetattr(sys.stdin)

        # Set the terminal to raw mode.
        tty.setraw(sys.stdin)

    def __del__(self):
        """
        Clean up the terminal.
        """

        # Restore the original terminal settings.
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.original_settings)

    def get_key(self):
        """
        Get a key from the terminal.
        """

        # Wait for a key press.
        while True:
            if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                break

        # Get the key press.
        key = sys.
