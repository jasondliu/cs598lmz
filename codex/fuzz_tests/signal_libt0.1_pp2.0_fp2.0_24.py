import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import QWidget, QVBoxLayout

class WebEngineView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(WebEngineView, self).__init__(*args, **kwargs)
        self.setWindowTitle('PyQt5 WebEngineView')
        self.resize(900, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = WebEngineView()
    view.load(QUrl('https://www.google.com'))
    sys.exit(app.exec_())
