import sys, threading

def run():
	from PyQt5.QtWidgets import QApplication
	from .MainWindow import MainWindow
	from .WindowGenerics import createWindowForFile
	
	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	
	# Create windows for open files
	from . import globVol
	from . import editorTabs
	from . import filetypes
	from . import editor
	from . import mainWindow
	mainWindow.mainwindow = w
	editorTabs.editorTabs = None # Don't try to create editor tabs
	for fn in sys.argv[1:]:
		ftype = filetypes.getFileType(fn)
		if ftype is None:
			sys.exit('File\'s extension %s is not recognized, aborting...' % fn)
		createWindowForFile(fn, ftype)
	
	sys.exit(app.exec_())

class WaitForDebugger(threading.Thread):
	def run(self):
		while 1:
			time
