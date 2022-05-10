import gc, weakref, sys
# import inspect

__all__ = []

class TestFeedback:

    __slots__ = []

    def __init__(self, name=None, fbI=None, fbO=None):
        self.name = name
        self.fbI = fbI
        self.fbO = fbO

    def feedback(self, fbItem):
        if self.fbI is not None:
            self.fbI.feedback(fbItem)
        self.fbO(fbItem)

    def __call__(self, fbItem):
        self.feedback(fbItem)

class TestFeedbackIO:

    __slots__ = ['test', 'tests']
    test = None
    tests = None
    _test_to_run = None

    def __init__(self, *oargs, **nargs):
        self.test = nargs.get('test', None)
        self.tests = nargs.get('tests', None)
        self._test_to_run = nargs.get('_test_to
