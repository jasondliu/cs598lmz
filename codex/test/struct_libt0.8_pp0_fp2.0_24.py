import _struct
# https://docs.python.org/3/library/struct.html

from iota import TryteString
# https://pypi.org/project/PyOTA/

from io import StringIO

def int2bytes(value):
    '''
    Converts an integer to bytes
    Arguments:
        value: int
    Return:
        bytes
    '''
    return _struct.pack('<q', value)

def bytes2int(value):
    '''
    Converts bytes to an integer
    Arguments:
        value: bytes
    Return:
        int
    '''
    return _struct.unpack('<q', value)[0]

def int2trytes(value):
    '''
    Converts an integer to trytes
    Arguments:
        value: int
    Return:
        trytes
    '''
    return TryteString.from_bytes(int2bytes(value)).decode()

