import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase
from frontend import Frontend

app = QApplication(sys.argv)
QFontDatabase.addApplicationFont("font/Quicksand-Bold.ttf")
QFontDatabase.addApplicationFont("font/Quicksand-Regular.ttf")

frontend = Frontend()
frontend.show()

sys.exit(app.exec_())
