import types
types.ClassType = type

def _print(output):
    """
    Prints a message, and ensures that the output is immediately flushed,
    so that AJAX requests don't have to wait for a full buffer to be flushed.
    """
