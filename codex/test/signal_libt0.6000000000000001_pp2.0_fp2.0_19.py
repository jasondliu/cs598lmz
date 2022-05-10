import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Add a custom logger to the root logger
logger = logging.getLogger()

# Create a handler to print the logs
ch = logging.StreamHandler()

# Set the level of the logger as debug
ch.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the handler
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)

# Configure the logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Create a new QApplication
app = QApplication(sys.argv)

# Create the main window
window = MainWindow()

# Show the window

