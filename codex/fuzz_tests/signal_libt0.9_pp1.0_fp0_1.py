import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) 

class settingsdialog(QDialog, Ui_settings):
    def __init__(self, version, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.version = version
        self.parent = parent
        self.setGeometry(300, 200, self.width(), self.height()) 
        self.ConnectSignalSlot()
        self.ShowSettings()
    
    def ConnectSignalSlot(self):
        self.buttonBox.accepted.connect(self.SaveSetting)

    def ShowSettings(self):
        try:
            self.dbConn = sqlite3.connect(config.dbName)
            self.dbCursor = self.dbConn.cursor()
            self.dbCursor.execute("SELECT VERSION FROM VERSION")
            version = self.dbCursor.fetchone()
            if version[0] != self.version:
                QMessageBox.
