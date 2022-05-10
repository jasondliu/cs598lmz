import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# create a Qt application
app = QApplication(sys.argv)

# create the widget
w = QWidget()
w.setWindowTitle('Simple')
w.show()

# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
