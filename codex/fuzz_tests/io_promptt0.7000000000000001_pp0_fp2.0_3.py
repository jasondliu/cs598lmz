import io
# Test io.RawIOBase
from io import RawIOBase
# Test io.BufferedIOBase
from io import BufferedIOBase
# Test io.TextIOBase
from io import TextIOBase


# Test exception processing.

def test_exception_args():
    """Test that sys.exc_info() returns argument tuple."""
    def f():
        raise Exception, "foo", "bar"
    try:
        f()
    except:
        e = sys.exc_info()[1]
        assert e.args == ("foo", "bar")


def test_exception_attributes():
    """Test that exception attributes can be set."""
    class AttributeException(Exception):
        def __init__(self, *args):
            self.args = args
            self.attribute = "foo"
    try:
        raise AttributeException
    except:
        e = sys.exc_info()[1]
        assert e.args == ()
        assert e.attribute == "foo"


def test_exception_message():
    """Test that exceptions can be instantiated without arguments."""
