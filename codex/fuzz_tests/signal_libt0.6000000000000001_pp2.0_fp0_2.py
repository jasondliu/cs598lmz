import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Qt Application
app = QtGui.QApplication(sys.argv)
app.setApplicationName('3D Slicer - Python Console')

# Main window
w = QtGui.QMainWindow()
w.setWindowTitle('3D Slicer - Python Console')
w.resize(600, 600)

# Icon
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap(':/Icons/AppIcon2.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
w.setWindowIcon(icon)

# Central widget
cw = QtGui.QWidget()
w.setCentralWidget(cw)

# Layout
layout = QtGui.QVBoxLayout()
cw.setLayout(layout)

# Text editor
editor = QtGui.QTextEdit()
layout.addWidget(editor)

# Button
button = QtGui.QPush
