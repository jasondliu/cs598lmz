import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from ui.main_ui import GeneralUI

app = QApplication(sys.argv)
window = GeneralUI()
window.show()
app.exec_()
