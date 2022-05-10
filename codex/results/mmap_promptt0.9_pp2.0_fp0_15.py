import mmap
# Test mmap.mmap().close() with some writing


def print_map(_map, offset, size):
    """Try to print all contents in given map."""
    try:
        print(_map[offset:offset + size])
    except Exception, why:
        print('ERROR: ma
