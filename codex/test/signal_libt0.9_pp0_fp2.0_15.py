import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui

import sys,os,re
"""
Functions
"""
def searchFiles(directory, extension, regexp):
    items = os.listdir(directory)
    dirs = [x for x in items if os.path.isdir(os.path.join(directory,x))]
    files = [x for x in items if os.path.isfile(os.path.join(directory,x)) and re.match(regexp, x, re.I) and x[-len(extension):] == extension]
    return dirs, files

"""
Classes
"""
#class for rendering the main window
class mainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        
        #set up the main window
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("Selects SolidWorks Files")
       
