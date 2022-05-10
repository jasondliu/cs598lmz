import gc, weakref
import re

class Regex(object):
    """A regular expression.

    This class behaves differently from the Python regular expression
    class: instead of compiling to an opaque Python object, it is
    represented by a string.

    This class is mainly used for argument passing: it is used to
    create a type for Regex arguments of functions.

    """

    def __init__(self, pattern):
        self.pattern = pattern
        if isinstance(pattern, Regex):
            pattern = pattern.pattern
        self._cre = re.compile(pattern)

    def __repr__(self):
        return 'Regex(%r)' % self.pattern

    def match(self, string):
        return self._cre.search(string)

    def search(self, string):
        return self._cre.search(string)

    def launch(self, string, **flags):
        return self._cre.search(string, **flags)

    def __eq__(self, other):
        return self.pattern == other.pattern


