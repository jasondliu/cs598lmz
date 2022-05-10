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
sys.exit(app.exec_())
</code>
I'm using PyQt4 and Python 2.7.3.
Thanks.


A:

I'm not sure if this is a bug in Qt or if it's just a weird side effect of the way the <code>ui_mainwindow</code> module is generated.  In any case, you can fix the problem by calling <code>setupUi</code> on the <code>MainWindow</code> object instead of on the <code>Ui_MainWindow</code> object:
<code>MainWindow.setupUi(Main
