import ctypes
# Test ctypes.CFUNCTYPE


@contextlib.contextmanager
def assert_raises_wintypes_error(err, msg=None):
    """Check if ctypes.WinError is raised with specific error number and message."""
    try:
        yield
    except ctypes.WinError as e:
        if e.winerror != err:
            raise AssertionError("expected winerror {} but got {}.".format(
                err, e.winerror))
        if msg is not None and msg not in str(e):
            raise AssertionError("expected exception message to contain '{}' but got '{}'.".format(
                msg, str(e)))
    else:
        raise AssertionError("expected ctypes.WinError to be raised.")


@contextlib.contextmanager
def assert_raises_nosuchprocess():
    """Check if NoSuchProcessError is raised."""
    try:
        yield
    except psutil.NoSuchProcess:
        pass
    else:
        raise AssertionError("expected psutil.NoSuchProcess to be raised.")


@contextlib.
