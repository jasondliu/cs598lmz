import weakref

from ncclient.xml_ import BASE_NS_1_0


class Send(object):
    
    def __init__(self, target, prefix, data, parent):
        self._tag = "{%s}%s" % (BASE_NS_1_0, self._type)
        self._prefix = prefix
        self._target = target
        self._data = data
        self._parent = weakref.ref(parent)
    
    def rewrite(self):
        "Return a new XML element with the rewritten infoset"
        return self._data
    
    def execute(self):
        "Send to target an XML element with the rewritten infoset"
        element = self.rewrite()
        self._parent()._write(element)
        return self._parent()
    
    def display(self, stream=sys.stdout):
        "Display the rewrite of the XML data to the stream"
        element = self.rewrite()
        dt = ElementTree.ElementTree(element)
        dt.write(stream, "utf-8")
