import weakref

class Operation:
    """
    The class of all operations.
    """

    def __init__(self):
        pass

    def run(self, start_index):
        """
        Run the operation on the document starting at start_index, and return the index just after the region
        affected by the operation.

        This is meant to be overridden by subclasses.
        """
        return 0

    def execute(self, document):
        """
        Executes the operation on the given document.
        """
        self.run(0)

    def update_cursor(self, cursor):
        """
        Updates the cursor to reflect the cursor's new position after the operation.
        """
        pass

class Modify(Operation):
    """
    The base class of all operations that modify the document.
    """

    def __init__(self):
        Operation.__init__(self)
        self.start_index = 0
        self.end_index = 0
        self.document = None

    def run(self, start_index):
        self.start_index =
