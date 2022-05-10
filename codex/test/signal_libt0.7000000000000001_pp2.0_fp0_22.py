import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.database_manager import DatabaseManager

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DatabaseManager()
    main_window = MainWindow(db)

    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())
