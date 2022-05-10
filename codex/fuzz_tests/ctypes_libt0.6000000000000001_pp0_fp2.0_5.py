import ctypes
ctypes.windll.user32.SetProcessDPIAware()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Карточка сотрудника")
        self.resize(300, 300)

        self.label1 = QtWidgets.QLabel("Фамилия", self)
        self.label1.move(50, 20)
        self.label2 = QtWidgets.QLabel("Имя", self)
        self.label2.move(50, 60)
        self.label3 = QtWidgets.QLabel("Отчество", self)
        self.label3.move(50, 100)
        self.label4 = QtWidgets.QLabel("Должность", self)

