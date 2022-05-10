fn = lambda: None
# Test fn.__code__.co_filename is set to the module name, not the __file__
pytest.register_assert_rewrite('_pytest.python')


HAS_INSPECT = True
try:
    from inspect import signature
except ImportError:
    try:
        from funcsigs import signature
    except ImportError:
        HAS_INSPECT = False


def all_matching_indices(seq, condition):
    """Generate all indices in ``seq`` that match ``condition``.

    Args:
        seq (sequence): The sequence to iterate through.
        condition (callable): A predicate that takes a single argument and
            returns true if the argument matches.

    Yields:
        int: The index of a value that matches the ``condition``.

    Example::

        >>> [i for i in all_matching_indices(['a', 'b', 'a'], lambda x: x == 'a')]
        [0, 2]

    """
    for i, item in enumerate(seq):
        if condition(item):
            yield i


def
