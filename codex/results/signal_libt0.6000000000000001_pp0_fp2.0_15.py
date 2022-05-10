import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# create a Qt application --- every PyQt app needs one
app = QApplication(sys.argv)

# Make a widget
win = QMainWindow()
win.setWindowTitle('pyqtgraph example: PlotWidget')
cw = QWidget()
win.setCentralWidget(cw)
layout = QGridLayout()
cw.setLayout(layout)

# Create the plot
pw = pg.PlotWidget(name='Plot1', title='Plot1')
layout.addWidget(pw, 0, 0)

# Plot something
pw.plot([1,2,4,8,16,8,4,2,1])

# Start the Qt event loop
win.show()
app.exec_()

</code>

