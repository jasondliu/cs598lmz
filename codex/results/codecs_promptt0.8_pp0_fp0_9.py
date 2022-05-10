import codecs
# Test codecs.register_error("strict", ...)

import re
import functools

import pytest


def test_register_error():
    # Test whether codecs.register_error actually replaces the old error
    # handler.
    def strict_error(*args):
        raise UnicodeError(*args)
    codecs.register_error("strict", strict_error)
    s = '\xff'
    assert s.encode('latin-1', 'strict') == b'\xff'
    with pytest.raises(UnicodeError):
        s.encode('ascii', 'strict')
    codecs.register_error("strict", None)
    s = '\xff'
    assert s.encode('latin-1', 'strict') == b'\xff'
    # Noncompliant behavior
    assert s.encode('ascii', 'strict') == (b'?', 1)

def test_register_error_bad():
    # Test whether register_error checks for the number of arguments
    def func0(): pass
    def func2
