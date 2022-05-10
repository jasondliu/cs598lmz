import select
# Test select.select()

def test():
    """Test select.select()."""

    # First argument must be a sequence type
    try:
        select.select(None, None, None, 0.0)
    except TypeError:
        pass
