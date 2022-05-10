import codecs
# Test codecs.register_error
# Ref: https://stackoverflow.com/a/4992490/133425
class MyError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        print("called in __init__()")

class MySubstitute(object):
    """docstring for MySubstitute."""

    def __init__(self, arg):
        self.arg = arg

    def __repr__(self):
        return "MySubtitute"

def my_handler(e):
    raise MyError("my_handler", "my bad")

codecs.register_error("my_error", my_handler)

try:
    codecs.decode("not a real codec", "ascii", "my_error")
except MyError as err:
    print("My error occured")
    print("e.expression:{0
