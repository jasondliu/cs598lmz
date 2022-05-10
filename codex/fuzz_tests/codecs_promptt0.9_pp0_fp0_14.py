import codecs
# Test codecs.register_error

# Test codecs.register_error()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')
log = logging.getLogger('test')

DEFAULT_ERROR = 'strict'

class MyTestException(Exception):
    def __init__(self, obj):
        self.obj = obj
    def __str__(self):
        return "MyTestException"

class MyTestError(LookupError, ValueError):
    def __init__(self, obj, start=None, end=None):
        self.obj = obj
        self.start = start
        self.end = end
    def __str__(self):
        return "MyTestError"

def my_strict_errors(exc):
    if isinstance(exc, MyTestException):
        msg = "strict error handling not allowed with MyTestException"
        raise ValueError(
