import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class QApp(QApplication):
    def __init__(self, *args, **kwargs):
        super(QApp, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), 'icon/icon.png')))


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('PyQt5学习教程')
        self.resize(600, 400)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)

        self.setToolTip('今天是<b>星期五</b>')
        self.setToolTipDuration(10000)

        self
