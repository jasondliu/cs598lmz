import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# create a Qt application - everything is started from here
app = QtGui.QApplication([])

# create the widget containing our visualization and giving it the title
w = QtGui.QWidget()
w.setWindowTitle('my first window')

# create a vertical box layout widget
vbox = QtGui.QVBoxLayout()

# add our visualization to the vertical box
vbox.addWidget(vispy_widget)

# set the vbox as the window's main layout
w.setLayout(vbox)

# show the window
w.show()

# start the Qt event loop
