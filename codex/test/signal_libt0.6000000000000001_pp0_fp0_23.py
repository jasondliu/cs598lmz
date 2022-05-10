import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from .main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Grammalecte")
    app.setWindowIcon(QIcon(":/QtGrammalecte/grammalecte.png"))
    window = MainWindow()
    window.show()
    return app.exec_()
