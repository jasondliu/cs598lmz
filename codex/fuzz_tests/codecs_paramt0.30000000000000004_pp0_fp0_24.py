import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__

class _Null(object):
    """
    A class that does nothing
    """
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, name):
        return self

    def __setattr__(self, name, value):
        pass

    def __delattr__(self, name):
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return False

    def __getitem__(self, name):
        return self

    def __setitem__(self, name, value):
        pass

    def __delitem__(self, name):
        pass

    def __repr__(self):
        return "<Null>"

    def __str__(self):
        return "Null"

    def __nonzero__(self):
        return False

    def
