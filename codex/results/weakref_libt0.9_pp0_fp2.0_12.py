import weakref
import time
import os
import warnings

# This can be replaced with logging package, but that's another dependency
def dolog(arg):
    print arg

def qdump__QObject(d, value):
    #warnings.warn("QObject dumping not thoroughly tested yet.")
    d.putEmptyValue()
    d.putNumChild(1)
    if d.isExpanded():
        with Children(d, 1, childType=0):
            d.putSubItem(QObjectData(d.extractPointer(value)))

class QObjectData:
    def __init__(self, qtAddress):
        self.qtAddress = qtAddress
        self.qtClass = 0

    def children(self):
        yield self.qtClass

    def display_hint(self):
        return "map"

def qdump__QObject__QObjectPrivate(d, value):
    d_ptr = value["d_ptr"]["d"]
    if isNull(d_ptr):
        d.putValue("(null)")
        d.putNum
