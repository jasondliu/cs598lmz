import bz2
# Test BZ2Decompressor
with bz2.BZ2File('', 'r') as f:
    # invalid mode
    try:
        f.mode = 'r'
        pass
    except AttributeError:
        pass
    # invalid filters
    try:
        f.filters = []
        pass
    except AttributeError:
        pass
    # invalid name
    try:
        f.name = 'a'
        pass
    except AttributeError:
        pass
    # invalid _buffer
    try:
        f._buffer = 'a'
        pass
    except AttributeError:
        pass
    # invalid _decompressor
    try:
        f._decompressor = 'a'
        pass
    except AttributeError:
        pass
    # invalid _buffer
    try:
        f._buffer = 'a'
        pass
    except AttributeError:
        pass

# Test BZ2Compressor
with bz2.BZ2Compressor() as f:
    # invalid name
    try:
        f.name = 'a'
        pass

