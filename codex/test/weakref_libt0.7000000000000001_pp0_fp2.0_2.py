import weakref

class ObservableList(list):

    def __init__(self, items=None):
        if items is None:
            items = []
        super(ObservableList, self).__init__(items)
        self.listeners = weakref.WeakKeyDictionary()

    def addListener(self, listener):
        self.listeners[listener] = 1

    def removeListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def addItem(self, item):
        self.append(item)
        self.notifyListeners()

    def removeItem(self, item):
        self.remove(item)
        self.notifyListeners()

    def notifyListeners(self):
        for listener in self.listeners.keys():
            listener.updateItems(self)
