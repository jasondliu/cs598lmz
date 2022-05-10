import select
# Test select.select()

def test_select():
    """
    >>> import select
    >>> select.select([],[],[])
    ([], [], [])
    """

def test_select_timeout():
    """
    >>> import select
    >>> select.select([],[],[],0.1)
    ([], [], [])
    """

def test_select_timeout_0():
    """
    >>> import select
    >>> select.select([],[],[],0)
    ([], [], [])
    """

def test_select_timeout_negative():
    """
    >>> import select
    >>> select.select([],[],[],-1)
    ([], [], [])
    """

def test_select_timeout_infinity():
    """
    >>> import select
    >>> select.select([],[],[],None)
    ([], [], [])
    """

def test_select_timeout_float():
    """
    >>> import select
    >>> select.select([],[],[],0.1)
    ([], [], [])
    """

def test
