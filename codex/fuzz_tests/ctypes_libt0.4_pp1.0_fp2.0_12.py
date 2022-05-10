import ctypes
ctypes.windll.user32.SetProcessDPIAware()


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.png'))
    ex = Example()
    sys.exit(app.exec_())


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.show()


if __name__ == '__main__':
    main()
