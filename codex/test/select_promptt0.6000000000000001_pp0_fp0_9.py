import select
# Test select.select with bad file descriptors.
try:
    select.select([-1], [-1], [-1])
    raise RuntimeError("select.select did not raise an exception")
except ValueError:
    pass
except OSError:
    # Some platforms can raise an OSError.
    pass
