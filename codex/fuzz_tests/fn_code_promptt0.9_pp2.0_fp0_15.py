fn = lambda: None
# Test fn.__code__
""")

import my_test_module


def foo_return_two():
    """Returns an int.

    :rtype: int
    """
    return 1 + 1


def foo_return_str():
    """Retur
