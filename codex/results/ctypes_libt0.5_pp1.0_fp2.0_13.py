import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Create the QApplication
app = QApplication(sys.argv)
# The Main window
w = QMainWindow()
w.setWindowTitle('Test')
# The QWidget widget is the base class of all user interface objects in PyQt4.
w.setCentralWidget(QWidget(w))
w.show()

# Execute app
sys.exit(app.exec_())
</code>

