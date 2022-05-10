import weakref

#
# this module implements an XPath 2.0 object model
#

# types

class NodeList(list):
    def __str__(self):
        return ''.join([str(x) for x in self])
    __repr__ = __str__

class Node(object):
    def __init__(self):
        pass
    def children(self):
        raise Exception("abstract")
    def stringValue(self):
        return str(self)
    def children(self):
        return NodeList()
    def __str__(self):
        return ''.join([str(n) for n in self.children()])
    __repr__ = __str__

class Element(Node):
    def __init__(self, tag='', *children):
        Node.__init__(self)
        self.tag = tag
        self.attrs = {}
        self.children = NodeList(children)
    def addAttr(self, key, value):
        self.attrs[key] = value
