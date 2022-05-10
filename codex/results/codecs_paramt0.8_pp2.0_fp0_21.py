import codecs
codecs.register_error('strict', codecs.ignore_errors)

def convert(filename):
    """
    converts a file of bytes

    >>> convert('test-data/animals.s16le')
    >>> convert('test-data/animals.s16be')
    >>> convert('test-data/animals.s24le')
    >>> convert('test-data/animals.s24be')
    >>> convert('test-data/animals.s32le')
    >>> convert('test-data/animals.s32be')
    >>> convert('test-data/animals.float')
    >>> convert('test-data/animals.double')

    >>> convert('test-data/animals.s16le', outfilename='test-data/animals.s16be')
    >>> convert('test-data/animals.s16be', outfilename='test-data/animals.s16le')
    >>> convert('test-data/animals.s24le', outfilename='test-data/animals.s24be')
    >>> convert('test-data/animals.s24
