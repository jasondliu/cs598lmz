import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# app = QtGui.QApplication(sys.argv)
app = QtWidgets.QApplication(sys.argv)

# from PyQt5 import QtCore, QtGui, QtWidgets

import argparse

# parser = argparse.ArgumentParser(description='Display a list of plots.')
parser.add_argument('--port', default=8080, type=int)
parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('--debug', action='store_true')
parser.add_argument('--no-browser', action='store_true')

args = parser.parse_args()

# port = args.port
# host = args.host

# if host == '0.0.0.0':
#     local_url = 'http://localhost:%d/' % port
# else:
