import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

class Microwave(QMainWindow):

    def __init__(self, parent=None):
        super(Microwave, self).__init__(parent)
        uic.loadUi('microwave.ui', self)
        self.setWindowTitle('Microwave')
        self.setWindowIcon(QIcon('microwave.ico'))
        self.show()

        welcome_song = QSound('welcome.wav')
        welcome_song.play()

        self.start_btn.clicked.connect(lambda: self.start())
        self.stop_btn.clicked.connect(lambda: self.stop())
        self.reset_btn.clicked.connect(lambda: self.reset())

        self.time_radiobtn.clicked.connect(lambda: self.set_limit('time'))
        self.power_radiobtn.clicked.connect(lambda: self.set_limit('power'))

    def set_limit(self, limit
