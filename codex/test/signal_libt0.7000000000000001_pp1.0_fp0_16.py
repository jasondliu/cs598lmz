import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt4 import QtGui, QtCore

class KinematicsEditor(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Kinematics Editor')
        self.setGeometry(50, 50, 800, 800)
        self.setToolTip('This is Kinematics Editor')
        self.detect_timer = QtCore.QTimer()
        self.detect_timer.timeout.connect(self.detect_kinematics)

        self.setup_ui()
        self.setLayout(self.layout)

    def setup_ui(self):
        self.layout = QtGui.QVBoxLayout()
        self.joint_edit_groupbox = QtGui.QGroupBox('Joint Edit')
        self.joint_edit_groupbox.setLayout(QtGui.QGridLayout())

