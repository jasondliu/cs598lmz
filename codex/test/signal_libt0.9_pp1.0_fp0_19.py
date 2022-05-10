import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

try:
    reload(sys)
except:
    pass

def notificar(texto, *args):
    global window
    QMessageBox.information(window, "AnterMT2", texto)

def AbrirURL(url):
    import webbrowser
    webbrowser.open_new(url)

class MainApp(QMainWindow):
    def __init__(self):
        global window
        global rootDir
        global pythonpath
        super(MainApp, self).__init__()
        uic.loadUi(rootDir + "/forms/MainWindow.ui", self)
        self.LbBackground.setStyleSheet("background: url(" + rootDir + "/imagens/main.png" + ");")
        self.LbBackground.setObjectName("LbBackground")
        self.LbBackground.setMinimumSize(1366, 768)
        self.LbBackground.setMaximumSize(1366, 768)
