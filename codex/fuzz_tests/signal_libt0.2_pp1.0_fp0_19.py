import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys

app = QApplication(sys.argv)

view = QWebEngineView()
view.load(QUrl("http://www.google.com"))
view.show()

sys.exit(app.exec_())
</code>

