import weakref

from . import tk


class _Mock(object):
    """
    A mock object that returns itself on any attribute access.
    """

    def __getattr__(self, name):
        return self


class _MockTk(tk.Tk):
    """
    A mock Tk object that returns itself on any attribute access.
    """

    def __init__(self):
        self._mock = _Mock()

    def __getattr__(self, name):
        return self._mock


class MockTk(object):
    """
    A context manager that replaces ``tkinter.Tk()`` with a mock object.

    The mock object returns itself on any attribute access.

    The original ``tkinter.Tk`` is restored when the context manager exits.
    """

    def __init__(self):
        self._tk = tk.Tk

    def __enter__(self):
        tk.Tk = _MockTk
        return self

    def __exit__(self, exc_type, exc_val, exc
