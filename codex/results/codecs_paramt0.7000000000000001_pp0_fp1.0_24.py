import codecs
codecs.register_error('strict', codecs.ignore_errors)
codecs.register_error('ignore', codecs.ignore_errors)

class CaptureHandler(logging.Handler):
    """
    A logging handler class which writes formatted logging records to
    a file on disk.
    """

    def __init__(self, filename, mode, encoding=None, delay=0):
        """
        Open the specified file and set up the handler.
        """
        logging.Handler.__init__(self)
        if codecs is None:
            encoding = None
        if encoding is None:
            self.stream = open(filename, mode)
        else:
            self.stream = codecs.open(filename, mode, encoding, 'strict')
        self.queue = queue.Queue(-1)
        t = threading.Thread(target=self.receive)
        t.daemon = True
        t.start()

    def setFormatter(self, fmt):
        logging.Handler.setFormatter(self, fmt)
        self.formatter = fmt

    def receive(self):

