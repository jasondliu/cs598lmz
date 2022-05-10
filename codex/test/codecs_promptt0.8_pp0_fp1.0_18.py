import codecs
# Test codecs.register_error method.

class MyException(Exception):
    def __init__(self, message):
        self.message = message

# Test callback that replaces 'X' by 'Y', and raises a MyException exception
# with 'x' and 'y' as arguments on encoding, and the opposite on decoding.

def error_handler(error):
    if error.end:
        s = error.object[error.start:error.end]
    else:
        s = error.object[error.start:]
    if error.name == "strict":
        # Encoding: replace 'X' by 'Y', but raises an exception for 'x'.
        # Decoding: replace 'Y' by 'X', but raises an exception for 'y'.
        s = s.replace(error.encoding[0], error.encoding[1])
