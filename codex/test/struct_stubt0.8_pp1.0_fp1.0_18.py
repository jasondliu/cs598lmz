from _struct import Struct
s = Struct.__new__(Struct)
s

# A class that recursively contains itself
class Node: 
  def __init__(self, parent= None, children=None): 
    self.parent = parent 
    if children is not None:
      self.children = children 
    else: 
      self.children = []
  def __repr__(self): 
    return '%s(parent=%r, children=%r)' % (type(self).__name__, self.parent and self.parent.parent, self.children)

root = Node()
root.children.append(Node(parent=root))
root.children.append(Node(parent=root))
root.children[0].children.append(Node(parent=root.children[0]))
root.children[0].children[0].children.append(Node(parent=root.children[0].children[0]))
root.children[0].children[0].children[0].children.append(Node(parent=root.children[0].children[0].children[0]))
