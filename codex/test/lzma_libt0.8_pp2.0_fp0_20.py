import lzma
lzma.DECOMPRESS_BUFFER_SIZE=(1<<25)
###############################################################################
# Nested Dictionaries
###############################################################################
def get_hash(x):
    """
    Returns a hash for the given object.
    """
    return hash(pprint.pformat(x))

def recursive_update(a, b):
    """
    Recursively update dictionary a with dictionary b.
    This will overwrite keys in a with values from b if b is a dict.
    """
    for k, v in b.items():
        if isinstance(v, dict):
            recursive_update(a.setdefault(k, {}), v)
        else:
            a[k] = v
    return a

def recursive_defaultdict():
    """
    Create a recursive default dictionary, such that any missing key is
    automatically created as another recursive_defaultdict, until reaching a
    terminal dict value, represented by the empty dict.
    """
    return defaultdict(recursive_defaultdict)

