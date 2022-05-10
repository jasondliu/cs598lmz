import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # зададим заголовок
        self.setWindowTitle("Тест")

        # зададим фоновое изображение
        self.setStyleSheet("background-image: url(img/pattern.png);")

        button1 = QtWidgets.QPushButton("Проверка", self)
        button1.setGeometry(10, 10, 110, 30)
        button1.clicked.connect(self.check)

    def check(self):
        self.window = TestWindow()
        self.window.show()


class TestWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__
