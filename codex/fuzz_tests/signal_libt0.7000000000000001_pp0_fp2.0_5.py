import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class Ui_MainWindow(object):

    path = "."
    current_file = "untitled.txt"
    current_dir = path
    current_font = "Plantagenet Cherokee"
    current_size = 14
    in_bold = False
    in_italic = False
    in_underline = False
    in_color = False
    color = QColor(255, 255, 255)
    fg = QColor(255, 255, 255)
    bg = QColor(0, 0, 0)

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addPixmap(QPixmap("resources/icon.png"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("central
