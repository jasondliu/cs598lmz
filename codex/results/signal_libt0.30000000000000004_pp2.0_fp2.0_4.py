import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView

app = QApplication(sys.argv)

view = QWebView()
view.load(QUrl("http://www.google.com"))
view.show()

sys.exit(app.exec_())
