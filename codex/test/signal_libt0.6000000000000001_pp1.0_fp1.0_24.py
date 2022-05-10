import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Set up logging
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)


class PyQtApp(QApplication):
    """
    QApplication with an exception hook.
    """

    def __init__(self, *argv):
        super().__init__(*argv)
        self.exception_hook = sys.excepthook
        sys.excepthook = self.handle_exception

