import weakref

#from . import compat
from . import _compat as compat

from . import util
from . import ltypes as types
from . import lvalues as values
from . import lerrors as errors


class Compiler(object):
    """
    Compiler for LiveScript source code. Compiled code will be executed in the
    same environment as the compiler.

    @ivar environment: the global environment
    @ivar debug: whether debugging info should be generated.
    """

    def __init__(self, environment=None, debug=False):
        if environment is None:
            from . import environment as environment
        self.environment = environment
        self.debug = debug
        self.next_uid = 0
        self.compile_cache = weakref.WeakKeyDictionary()

    def compile(self, source, filename=None, cached=True):
        """
        Compile LiveScript source code.

        @param source: the LiveScript source code
        @type source: C{str}
        @param filename: name of the source file
        @type filename: C{str}
       
