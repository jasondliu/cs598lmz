import weakref

from .util import _set_error, Error, ErrorDomain


def _null_paths(paths):
    if paths is None:
        return ()
    return paths


class View(GObject.Object):
    def __init__(self, window, name, text=None, line=None, column=None,
                 paths=None, uri=None):
        GObject.Object.__init__(self)

        self.__window = weakref.ref(window)
        self.__text = Text(self, name, text, paths, uri)

        if line is not None:
            line = max(0, line)
        else:
            line = 0
        if column is not None:
            column = max(0, column)
        else:
            column = 0
        self.__cursor = Cursor(self, line, column)

    def __repr__(self):
        if self.__window() is None:
            return '<View %r (%i)>' % (self.name, id(self))
        else:

