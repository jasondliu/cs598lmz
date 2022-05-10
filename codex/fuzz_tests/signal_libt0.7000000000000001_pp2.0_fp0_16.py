import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
import sys
from controller import MainWindow
from data import User
from data import Reservation


app = QApplication(sys.argv)
sys.excepthook = sys.__excepthook__

w = MainWindow()

w.setUser(User('lyc', '123456'))
w.setReservation(Reservation('test', 200, '2018-09-01', '2018-09-10', None))

sys.exit(app.exec_())
