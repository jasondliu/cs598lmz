import gc, weakref


class testMockup:
    """
    A mockup class.
    
    It is used to test C++ Qt5 classes.
    """

    def __init__(self):
        self.ref = None
        self.destroyed = False

    def __del__(self):
        self.destroyed = True

    def connection(self, sender, signal, receiver, slot, connection_type):
        self.ref = weakref.ref(sender)
        self.ref.connect(sender, signal, receiver, slot, connection_type)

    def sendSignal(self):
        self.ref().emitSignal()


