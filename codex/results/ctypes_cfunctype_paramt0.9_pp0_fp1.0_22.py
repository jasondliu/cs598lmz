import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool)

from dsi import DSI

class Report(object):
    """
    Describe a run of a test.

    :ivar start: Start time of the test.
    :ivar duration: Time taken for the test to complete (in seconds).
    :ivar iterations: Number of times the test was run.
    :ivar result: A collection of results. One item is recorded for each
        iteration.
    """

    def __init__(self, test, **arguments):
        """
        :param str test: Test identifier.
        :param list result: Collection of iteration results.
        """
        self.test = test
        self.start = None
        self.duration = None
        self.iterations = None
        self.result = []
        self.arguments = arguments

    def failed(self):
        """
        Was one or more iterations of the test unsuccessful?
        """
        for (_, _, failed) in self.result:
            if failed:
                return True
        return False

    def to_text(self):

