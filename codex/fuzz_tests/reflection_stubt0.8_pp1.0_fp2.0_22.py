fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


if __name__ == "__main__":
    import doctest
    doctest.testmod()
