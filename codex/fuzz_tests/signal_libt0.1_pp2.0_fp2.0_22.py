import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)

web = QWebEngineView()
web.load(QUrl("http://www.google.com"))
web.show()

sys.exit(app.exec_())
