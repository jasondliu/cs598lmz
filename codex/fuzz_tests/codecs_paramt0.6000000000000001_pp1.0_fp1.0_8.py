import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _lazy_load_data(fileobj):
    """
    A wrapper around a file-like object that lazily loads the data into memory
    when the ``readlines`` method is called.
    """
    class Memoize(object):
        def __init__(self, fileobj):
            self.fileobj = fileobj
            self.data = None

        def __getattr__(self, key):
            return getattr(self.fileobj, key)

        def readlines(self):
            if self.data is None:
                self.data = self.fileobj.readlines()
            return self.data

    return Memoize(fileobj)

def _load_from_module(module):
    """
    Loads the data from a module, given the module instance.
    """
    loader = getattr(module, 'load', None)
    if loader is not None:
        return loader()

    fileobj = getattr(module, '__file__', None)
    if fileobj is not None:
