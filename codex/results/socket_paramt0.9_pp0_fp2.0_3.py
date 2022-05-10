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
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception:
            print 'Unhandled exception'
            # print '-'*60
            # traceback.print_exc(file=sys.stdout)
            # print '-'*60
    return wrapper


@scoped_method_decorator
def scoped_method(function):
    return function


@class_method_decorator
def class_method(function):
    return function
# endregion


def arg_to_text(v):
    t = type(v)
    if t is dict:
        return
