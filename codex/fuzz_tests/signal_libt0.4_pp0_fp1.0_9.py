import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#
#  Create QApplication
#
app = QApplication(sys.argv)

#
#  Check to see if running from source.
#  If so, we need to add the examples/lib to the system path.
#
source_directory = os.path.dirname(os.path.abspath(__file__))
examples_directory = os.path.dirname(source_directory)
lib_directory = os.path.join(examples_directory, 'lib')
sys.path.insert(0, lib_directory)

#
# Create MainWindow and populate with a few widgets
#
window = QMainWindow()
window.setWindowTitle("Qt Examples")
window.setWindowIcon(QIcon(os.path.join(source_directory, 'qt-logo.png')))

#
#  Create a central widget for MainWindow and set it
#
central_widget = QWidget()
window.setCentralWidget(central_widget)

#
# 
