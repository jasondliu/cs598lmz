import sys, threading

def run():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec()

def output(str):
    print(str)

def runScript(script):
    if script == "1":
        script1()


def script1():
    ser = serial.Serial(2, 9600)
    while True:
        output(ser.readline().decode('utf-8'))
        time.sleep(1)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.box1 = QComboBox(self)
        self.box1.addItem("Press to choose COM")
        for elements in range(1, 11):
            self.box1.addItem(str(elements))

        self.box1.move(100, 100)
        self.box1.activated[str].connect(self.onChanged)

        self.box2 = QComboBox(self)
        self
