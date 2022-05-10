import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
###

import json
import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL, Qt
#my import
from view.mainwindowform import Ui_Form
from controller import MainController
from dbconnector import DBConnector
import_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(import_dir, '..', '..', '..', 'utils'))
from utils import dbgFuncCall, getAvailablePort, getAvailablePortForResponse

confdict = {
	'auth': {
		'login': 'sa',
		'password': ''
	},
	'connection': {
		'host': '',
		'port': 12345
	},
	'manager': {
		'path': os.path.join(import_dir, '..', '..', '..', '..', '..', '
