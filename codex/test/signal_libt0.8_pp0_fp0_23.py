import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

window = QtWidgets.QMainWindow()
window.resize(1024,600)

qt_app = QtWidgets.QApplication.instance()
app = qt_app.app
app.window = window

app.layout = QtWidgets.QWidget()
app.layout.setLayout(QtWidgets.QVBoxLayout())
app.layout.layout().setContentsMargins(0, 0, 0, 0)
app.layout.layout().setSpacing(0)

window.setCentralWidget(app.layout)

window.show()
window.setWindowTitle("DAZL")

window.setWindowIcon(QtGui.QIcon("static/icon.png"))

