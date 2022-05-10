import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()

# pyKlondike imports
from game import Game, GameException

# PyQt4 imports
from PyQt4.QtGui import QApplication
from ui.window import Window

def main():
    """ The main function responsible for starting the UI and the game. """

    app = QApplication(sys.argv)
    win = Window()
    game = Game(win)
    try:
        game.setup()
    except GameException as e:
        # TODO show messagebox
        print('Error:', e)
        exit()
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()
