import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("HSD")
        self.setWindowIcon(QIcon("HSDLogo.png"))

        self.mainScreen = MainScreenWidget(self)
        self.mainScreen.setGeometry(0, 0, 800, 600)
        self.mainScreen.showMaximized()

        self.highScore = HighScoreWidget(self)
        self.highScore.setGeometry(0, 0, 800, 600)
        self.highScore.hide()
        #self.highScore.showMaximized()

        self.info = InfoWidget(self)
        self.info.setGeometry(0, 0, 800, 600)
        self.info.hide()
        #self.info.showMaximized()

        self.settings = SettingsWidget(self)

