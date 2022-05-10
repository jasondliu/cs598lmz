import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the Qt Application
app = QApplication(sys.argv)
# Create and show the form
form = MainWindow()
form.show()
# Run the main Qt loop
sys.exit(app.exec_())
