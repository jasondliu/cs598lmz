import _struct
# Test _struct.Struct() with a single format string.
def test_s(s):
    '''
    >>> test_s('xxxx')
    Array 20 bytes
    9 12 79 79 79 79 79 79 79 79 79 79 79 79 79 79 79 79 79 79 79 79 79 79
    <BLANKLINE>
    >>> test_s('=f')
    Array 4 bytes
    52 64 210 203
    <BLANKLINE>
    >>> test_s('@f')
    Array 4 bytes
    52 64 210 203
    <BLANKLINE>
    >>> test_s('<f')
    Array 4 bytes
    52 64 210 203
    <BLANKLINE>
    >>> test_s('>f')
    Array 4 bytes
    52 64 210 203
    <BLANKLINE>
    >>> test_s('!f')
    Array 4 bytes
    207 211 64 52
    <BLANKLINE>
    >>> test_s('h')
    Array 2 bytes
    10 10
    <BLANKLINE>
    >>> test_s('@h')
    Array 2 bytes
    10 10
    <BLANKLINE
