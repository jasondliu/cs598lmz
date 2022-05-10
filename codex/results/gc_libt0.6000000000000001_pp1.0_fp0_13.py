import gc, weakref
from pypy.translator.backendopt.all import backend_optimizations
from pypy.translator.backendopt.all import INLINE_THRESHOLD_FOR_TEST
from pypy.translator.backendopt.all import INLINE_THRESHOLD_FOR_TEST_NOPY
from pypy.translator.backendopt.all import INLINE_THRESHOLD_FOR_TEST_PYPY
from pypy.translator.backendopt.all import INLINE_THRESHOLD_FOR_TEST_RPYTHON
from pypy.translator.backendopt.all import INLINE_THRESHOLD_FOR_TEST_RPYTHON_NOPY
from pypy.translator.backendopt.all import INLINE_THRESHOLD_FOR_TEST_RPYTHON_PYPY
from pypy.translator.backendopt.inlining import auto_inlining
from pypy.translator.backendopt.inlining import inline_function
from pyp
