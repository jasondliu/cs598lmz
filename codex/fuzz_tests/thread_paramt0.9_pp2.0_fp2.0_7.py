import sys, threading
threading.Thread(target=lambda:sys.stdout.write(""), daemon=True).start()

from PyQt5.Qt import *


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(75, 75)

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(25, 25, 25, 25))
        self.pushButton.setObjectName("pushButton")

    def __del__(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    QShortcut(QKeySequence("Ctrl+Q"), w, QApplication.exit)
    w.setCentralWidget(MyWindow())
    w.show()
    try:
        sys.exit(app.exec_())
    except:
        print('Exiting')
