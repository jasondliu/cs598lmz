import _struct
import types

log = logging.getLogger(sys._getframe().f_code.co_name)
warning = log.warning
info = log.info
debug = log.debug
error = log.error

def read(filename, size, pos=0):
    '''
    Read specified size of bytes from a file.
    '''
    with open(filename, 'rb') as f:
        f.seek(pos)
        return f.read(size)

def write(filename, buff, pos):
    '''
    Write binary data (buff) into end of specified file.
    '''
    with open(filename, 'ab+') as f:
        f.seek(pos)
        f.write(buff)

def fmap(type, filename, pos=0):
    '''
    Return multiple number of type object by packing binary data read from
    specified filename (file-like object) start from pos.
    '''

    buf = read(filename, _struct.calcsize(type) * len(target), pos=pos)

    pos +=
