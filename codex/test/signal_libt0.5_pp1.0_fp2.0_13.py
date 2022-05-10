import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Initialize the Qt application
app = QApplication(sys.argv)

# Import the compiled UI module
from ui import ui_mainwindow

# Create a QT4 window from the imported .ui file
window = ui_mainwindow.Ui_MainWindow()
window.setupUi(MainWindow)

# Show the window
MainWindow.show()

# Start the application's event loop
