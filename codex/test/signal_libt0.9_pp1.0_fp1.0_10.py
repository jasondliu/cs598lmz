import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
from PyQt4 import QtGui, QtCore
from art.props import globalProperties
import art
from daq.daq import DAQ
import time

class StartButton(QtGui.QPushButton):
	def __init__(self,artdaq):
		super(StartButton,self).__init__("Start DAQ")
		self.artdaq=artdaq
		self.clicked.connect(self.onClick)
		self.setSizePolicy(
			QtGui.QSizePolicy.Minimum,
			QtGui.QSizePolicy.Minimum,
		)

	def onClick(self):
		self.setEnabled(False)
		self.parent().saverButton.setEnabled(False)
#		self.artdaq.setProperty("daq.save_data","true")
		self.parent().filter.setEnabled(False)
		self.parent().daq.start()

