import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)


class Logger(object):

    def __init__(self, path, rank):
        self._file = open(path, "w")
        self._terminal = sys.stdout
        self._rank = rank

    def write(self, message):
        self._terminal.write(message)
        self._file.write("[rank {}] {}".format(self._rank, message))
        self._file.flush()

    def flush(self):
        self._file.flush()

class NoRankLogger(object):
    def __init__(self, path):
        self._file = open(path, "w")
        self._terminal = sys.stdout

    def write(self, message):
        self._terminal.write(message)
        self._file.write(message)
        self._file.flush()

    def flush(self):
        self._file.flush()
