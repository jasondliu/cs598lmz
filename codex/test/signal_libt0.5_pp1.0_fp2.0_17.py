import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Icons')

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('web.png')

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    sys.exit(app.exec_())
