import weakref

class MockWindow(object):
    def __init__(self):
        self.signals = {}
    def connect(self, signal, callback):
        self.signals[signal] = callback
    def emit(self, signal):
        self.signals[signal]()

class MockRenderCommand(object):
    def __init__(self, item, action):
        self.item = weakref.ref(item)
        self.action = action
        self.laid = False
        self.cleaned = False

    def lay(self, container, offset = (0,0)):
        self.laid = True
        self.container = container
        self.offset = offset

    def clean(self):
        self.cleaned = True

    def update(self):
        pass

class MockRenderDict(dict):
    def lay(self, container, offset = (0,0)):
        for cmd in self.values():
            cmd.lay(container, offset)

    def clean(self):
        for cmd in self.values():
            cmd
