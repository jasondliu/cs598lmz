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
