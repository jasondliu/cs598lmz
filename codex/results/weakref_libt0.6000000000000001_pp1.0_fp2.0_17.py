import weakref

class BinaryTree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

    def __str__(self, level=0, indent="    "):
        string = level*indent + repr(self.data) + "\n"
        if self.left:
            string += self.left.__str__(level+1, indent)
        if self.right:
            string += self.right.__str__(level+1, indent)
        return string

    def __repr__(self):
        return "<BinaryTree node %s>" % self.data

    def __eq__(self, other):
        if type(other) is type(self):
            return self.data == other.data
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

    def height(self
