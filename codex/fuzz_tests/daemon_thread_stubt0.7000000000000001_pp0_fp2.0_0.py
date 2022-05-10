import sys, threading

def run():
    time.sleep(1)
    os.system("python c://users/heaven/desktop/code/py/read.py")

t = threading.Thread(target=run)
t.start()

app = QApplication(sys.argv)

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.title = '計算機'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 500
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(500, 500)

        self.display = QLabel(self)
        self.display.setText("")
        self.display.setFont(QFont("Times", 20, QFont.Bold))
        self.display.setAlignment(Qt.AlignRight)

