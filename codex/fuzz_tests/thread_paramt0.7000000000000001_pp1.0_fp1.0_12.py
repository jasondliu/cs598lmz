import sys, threading
threading.Thread(target=lambda: sys.stdout.write("")).start()

def main():
    # This is the main function.
    # If the program is run as a script, this is where it will start.
    #
    # This is also where you can set the custom arguments for your game.
    # If you don't want to use command line arguments, you can also set
    # them directly here in this function.
    #
    # What follows is a complete list of the command line options for
    # Pygame Zero.
    #
    # -h, --help: show this help message and exit
    # -f, --fps: frames per second (default: 60)
    # -w, --width: screen width (default: 800)
    # -e, --height: screen height (default: 600)
    # -i, --interval: milliseconds between each frame (default: 0)
    # -d, --display: display mode (default: window)
    # -a, --audio: audio playback mode (default: openal)
    # --debug: enable debug mode
    # --virtual-pixel: enable
