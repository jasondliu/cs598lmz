import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Set up a logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('debug.log')
handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(handler)


class Application(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationName("Syntax-Highlighted Editor")
        self.setOrganizationName("FOSS@Amrita")
        self.setOrganizationDomain("foss.amrita.edu")
