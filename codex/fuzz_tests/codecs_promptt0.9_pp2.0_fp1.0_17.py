import codecs
# Test codecs.register_error("foo", codecs.replace_errors) for external errors
import codecs

from test import support

errors = [
    # bytesize, string, repr of expected exception
    (1, b"\xff", "'utf-8' codec can't decode byte 0xff in position 0: invalid start byte"),
    (1, b"\xdd\xff", "'utf-8' codec can't decode bytes in position 0-1: invalid continuation byte"),
    (2, b"a\xffb", "'utf-8' codec can't decode byte 0xff in position 1: invalid start byte"),
    (2, b"a\xdd\xffb", "'utf-8' codec can't decode bytes in position 1-2: invalid continuation byte"),
    (3, b"a\xdd\xffb\x00c", "'utf-8' codec can't decode bytes in position 1-2: invalid continuation byte"),
    (3, b"a\xffb\x00c", "'utf-8' codec can't decode byte 0xff in position 1: invalid start byte"),
    (4, b"a\x
