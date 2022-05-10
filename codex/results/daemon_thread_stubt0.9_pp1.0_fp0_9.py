import sys, threading

def run():
    print "send data into client 1"
    # I would like to send the data string in to the client 1?
    pass

def request(client):
    print "request server answer to client 1"
    # I would like to send this string as request to server and answer to client 1
    pass

sys.exit(connect())
</code>
Because the app has GUI, I need to run the GUI in main thread
<code>if __name__ == '__main__':
    from frontend.mainwindow import MainWindow
    from PyQt4.QtGui import *
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
</code>
How can I establish client-server connection between a program and its GUI?


A:

You can use <code>QtNetwork</code> module to make the TCP connection using <code>QTcpServer</code> and <code>QTcpSocket</code>.
<code>from PyQt4 import QtNetwork
from PyQt
