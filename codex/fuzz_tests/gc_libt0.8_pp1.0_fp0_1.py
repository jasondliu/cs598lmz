import gc, weakref


class LinkedList():
    """A doubly linked list.
    LinkedList is implemented as a class object for convenience (rather than
    a module or a struct).  It has a few extra attributes and methods (e.g.,
    insert(), find(), etc.), which makes it convenient to use.  The core
    attributes are:
      * self.next: the next node in the linked list
      * self.prev: the previous node in the linked list
    In addition, it has the following convenience methods:
      * insert(): inserts a given node after the current node.
      * find(): searches for a node in the linked list, starting at the
          current node.
      * remove(): removes the current node from the linked list.
    """
    def __init__(self, data=None):
        """Creates a new node.
        The arguments are:
          * data: the data to store in the node.  It can be anything, e.g.,
              a list, a dictionary, etc.  For convenience, when creating a
              LinkedList, you can pass a data item as the argument.

