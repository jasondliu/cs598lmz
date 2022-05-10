import socket

# pylint: disable=C0103,C0111,W0613
class Link(object):
    def __init__(self, to_node, from_node):
        self.to_node = to_node
        self.from_node = from_node
        self.to_node.add_incoming(self)
        self.from_node.add_outgoing(self)

    def __str__(self):
        return "(%s -> %s)" % (self.from_node, self.to_node)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.to_node.name) ^ hash(self.from_node.name)

class Node(object):
    def __init__(self, name):
        self.name = name
        self.incoming = []
        self.outgoing = []
        self._neighbors = None

    def __str__(self):
        return str(self.name)

