import select
# Test select.select()

def test():
    """Test select.select()."""

    # First argument must be a sequence type
    try:
        select.select(None, None, None, 0.0)
    except TypeError:
        pass
    else:
        print 'TypeError not raised'

    # Second and third arguments must be a sequence type or None
    try:
        select.select([], None, None, 0.0)
    except TypeError:
        pass
    else:
        print 'TypeError not raised'
    try:
        select.select([], [], None, 0.0)
    except TypeError:
        pass
    else:
        print 'TypeError not raised'

    # Fourth argument must be a float
    try:
        select.select([], [], [], 'foo')
    except TypeError:
        pass
    else:
        print 'TypeError not raised'

test()
