import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stderr.write("\n")
    sys.stderr.flush()

threading.Thread(target=run).start()

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWebKit import QWebSettings

app = QApplication(sys.argv)

web = QWebView()
web.setWindowTitle('Loading...')
web.setGeometry(0,0,800,600)
web.load(QUrl('http://localhost:8000'))
web.show()

sys.exit(app.exec_())
