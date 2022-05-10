import io
# Test io.RawIOBase in Python 2.
#
# To test the stdio wrapper, we use a stdio wrapper that records what
# arguments are passed to the underlying stdio function.
# This allows us to test that the arguments are correctly forwarded.
class StdioRecorder(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.calls = []

    @staticmethod
    def _record(method, *args, **kwargs):
        return lambda: method(*args, **kwargs)

    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)

    def write(self, *args, **kwargs):
        self.calls.append(self._record(self.wrapped.write, *args, **kwargs))

    def read(self, *args, **kwargs):
        self.calls.append(self._record(self.wrapped.read, *args, **kwargs))

