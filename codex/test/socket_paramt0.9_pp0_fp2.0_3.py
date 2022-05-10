import socket
socket.if_indextoname(3)

def example():
    """
    http://intellij-support.jetbrains.com/entries/23405018-Python-inspection-analysis-warnings-and-errors
    """

# region decorators
@exception_logger
def exception_decorator(function):
    """
    Decorator that logs to console.
    """
