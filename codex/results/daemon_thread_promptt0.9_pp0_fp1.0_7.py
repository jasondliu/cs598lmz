import threading
# Test threading daemon
import time

# Set Gui as tkinter
gui = tkinter


# Set printing at the end of an execution
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# Threading class to continue updating the GUI
class ThreadClass(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Starting " + self.name)
        run_game()
        print("Exiting " + self.name)


def setup():
    # Setting up the variables to be used in the actual game
    # Setting up first window screen
    topWindow = gui.Toplevel()
    topWindow.title("Welcome To Ludum Dare 29")
    topWindow.geometry("700x700")
    # Creating window for the game
    root = gui.Tk()
    root.lift()
    root.attributes("-topmost
