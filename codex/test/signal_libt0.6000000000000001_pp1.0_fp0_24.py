import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class StringIO(StringIO.StringIO):
    def __init__(self):
        StringIO.StringIO.__init__(self)
        self.encoding = 'utf-8'

class _FakeStdout(object):
    def __init__(self):
        self._buffer = StringIO()
        self.encoding = 'utf-8'
    def write(self, s):
        self._buffer.write(s)
    def getvalue(self):
        return self._buffer.getvalue()

def _execfile(filename, globals_, locals_):
    # for python 2.6, we use execfile
    if sys.version_info[:2] == (2, 6):
        execfile(filename, globals_, locals_)
    else:
        with open(filename, 'rb') as f:
            exec(compile(f.read(), filename, 'exec'), globals_, locals_)

