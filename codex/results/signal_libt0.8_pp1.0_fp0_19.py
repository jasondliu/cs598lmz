import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		#Setup GUI
		self.setupUI()

		#Connect Signals
		self.signals()

		#Init Processes
		self.initProcesses()

		#Detect available CAMs
		self.detectCAMS()

	def setupUI(self):
		#Global UI Variables
		self.lineEdit_detect = QtWidgets.QLineEdit(self)
		self.plainTextEdit_log = QtWidgets.QPlainTextEdit(self)
		self.plainTextEdit_log.setReadOnly(True)
		self.pushButton_detect = QtWidgets.QPushButton('Detect', self)
		self.pushButton_startRecording = QtWidgets.QPushButton('Start Recording', self)
		self.
