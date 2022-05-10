import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtCore import QEventLoop, QTimer

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QEventLoop, QTimer

app = QApplication([])

view = QWebEngineView()
view.load(QUrl("https://www.google.com"))
view.show()

loop = QEventLoop()
view.loadFinished.connect(loop.quit)
loop.exec_()

view.page().toHtml(lambda data: print(data))

loop = QEventLoop()
QTimer.singleShot(1000, loop.quit)
loop
