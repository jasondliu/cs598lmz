import select
# Test select.select()

def test_select():
    """
    >>> test_select()
    select.select() works
    """
    print "select.select() works"

def test_select_timeout():
    """
    >>> test_select_timeout()
    select.select() with timeout works
    """
    print "select.select() with timeout works"

def test_select_error():
    """
    >>> test_select_error()
    Traceback (most recent call last):
    ...
    ValueError: filedescriptor out of range in select()
    """
    select.select([], [], [], 0, -1)

def test_select_keyboard_interrupt():
    """
    >>> test_select_keyboard_interrupt()
    Traceback (most recent call last):
    ...
    KeyboardInterrupt
    """
    select.select([], [], [], 0, 1)

def test_select_bad_timeout():
    """
    >>> test_select_bad_timeout()
    Traceback (most recent call last):
    ...

