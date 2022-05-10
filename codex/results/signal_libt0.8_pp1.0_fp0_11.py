import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
DIR = os.path.dirname(os.path.realpath(__file__))

TOOLBAR_STYLE = '''
QToolBar {
  background: #131313;
  border: 2px solid #444;
}

QToolButton {
  min-width: 50px;
  max-width: 50px;
  padding: 0px 0px;
  margin: 0px 0px;
  border: 0px;
  background: #131313;
}

QToolButton:checked {
  background: #666;
}

QToolButton:hover {
  background: #333;
}
'''

class Window(QMainWindow):
    def __init__(self, *args):
        super(Window, self).__init__(*args)
        self.setWindowTitle("Simple Example")
        self.resize(300, 200)
        self.setMinimumSize(200, 200)
        self.setMaximumSize(400,
