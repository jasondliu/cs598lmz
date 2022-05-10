import sys, threading

def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(5)
    while True:
        client, address = server.accept()
        print 'Got connection from', address
        client.send('Thank you for connecting')
        client.close()

threading.Thread(target=run).start()

from PyQt4.QtCore import QUrl, QObject, pyqtSlot, QCoreApplication, Qt
from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt4.QtGui import QApplication

app = QApplication(sys.argv)

class MyClass(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self.handleFinished)

    def request(self):
        url = QUrl('http://localhost:8080')
        request
