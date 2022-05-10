import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class OutputError(Error):
    """Exception raised for errors in the output.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

def get_file_content(file_name, encoding='utf-8'):
    """
    get the content of a file
    """
    try:
        with codecs.open(file_name, 'r', encoding) as f:
            return f.read()
    except IOError:
        print("Error:
