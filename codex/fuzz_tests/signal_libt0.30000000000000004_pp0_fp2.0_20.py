import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# initialize Qt
app = QApplication(sys.argv)

# create the GUI
window = MainWindow()

# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
