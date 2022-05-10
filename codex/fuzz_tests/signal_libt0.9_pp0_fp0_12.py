import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class MainWindow(QMainWindow):
    def __init__(self, dbvars):
        """
        initilize main window class

        :param dbvars: dictionary of the following form:
            {'url': URL of the database, 'login': login_name, 'pwd': password}
        """
        # create main window
        QMainWindow.__init__(self)

        self.setObjectName("MainWindow")
        self.resize(639, 444)
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxVisualize = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxVisualize.setObjectName("groupBox
