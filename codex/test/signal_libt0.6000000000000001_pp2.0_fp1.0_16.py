import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtWidgets import QApplication
from ui.main import MainWindow
from core import Config


def main():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    c = Config()
    c.load_config('config.ini')
    main()
