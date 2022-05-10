import codecs
# Test codecs.register_error('my_error', codecs.replace_errors)

def test_decode_error(self):
    self.assertEqual(b"abc\xff".decode('ascii', 'my_error'),
                     u"abc\ufffd")
</code>
The test passes using Python 2.7.1 but not with Python 3.2.2:
<code>======================================================================
ERROR: test_decode_error (__main__.Test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test.py", line 8, in test_decode_error
    u"abc\ufffd")
AssertionError: 'abc\ufffd' != 'abc\ufffd'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
</code>
Is this a bug in Python 3.2.2?  I'm using the UTF-8 encoding.


A:

I wouldn't call this a bug.  What you are seeing is the difference between Python 2 and Python 3.  In Python 2, strings are sequences of bytes
