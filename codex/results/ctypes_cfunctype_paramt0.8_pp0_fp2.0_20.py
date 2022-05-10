import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, *(ctypes.c_int * 2) * 2)

def pair_sum(iterable, target):
    """Finds two numbers in iterable that sum up to the target.
    
    >>> pair_sum([1, 2, 3, 2], 4)
    (2, 3)
    >>> pair_sum([1, 2, 3, 2], 5) # Nothing to do
    ()
    """
    # Convert iterable to a list
    iterable = list(iterable)
    head, tail = iterable[0], iterable[1:]
    while tail:
        current_target = target - head
        try:
            return head, tail.index(current_target)
        except ValueError:
            head, tail = tail[0], tail[1:]
    return ()


def pair_sum_v2(iterable, target):
    """Finds two numbers in iterable that sum up to the target.
    Version 2 uses a Hash table to store the iterable values
    as keys and their positions as values. 

    >>> pair_sum_v2([
