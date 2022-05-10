import weakref

from log import createConsoleLogger, getLogger

# logging
that_logger = getLogger(__name__)

class OneShot(object):

    def __call__(self, func, *args, **kwargs):
        if not hasattr(self, "_called"):
            self._called = True
            return func(*args, **kwargs)
        else:
            raise ValueError("%s is a one-shot, it can only be called at most once."%self)


class FileRef(object):
    """
    Reference to a file that can be resolved later, rather than using a
    filename (for refactoring)
    """
    #### reference
    def _get_filename(self):
        if not self.__filename:
            if isinstance(self.__filename_f, OneShot):
                self.__filename = self.__filename_f()
            elif self.__filename_f:
                self.__filename = self.__filename_f
            elif "_filename" in self.__dict__:
                return self._filename
