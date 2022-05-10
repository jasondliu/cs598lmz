import weakref
# Test weakref.ref() with methods of containers.
import operator
SUPPORTED_TYPES = [bytes, bytearray, list, set, frozenset, dict]


def ref(obj):
    """Never raises TypeError."""
    if isinstance(obj, SUPPORTED_TYPES):
        return weakref.ref(obj)
    else:
        return None


def print_list(list):
    print(list)


def test():
    foo = ['eggs', 'spam']
    r = ref(foo.__len__)
    print_list(foo)
    print(r(), len(foo))
    foo.pop()
    print(r(), len(foo))


try:
    test()
except TypeError as msg:
    print(msg)
