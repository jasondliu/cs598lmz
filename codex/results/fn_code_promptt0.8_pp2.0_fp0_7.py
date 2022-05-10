fn = lambda: None
# Test fn.__code__

# _imp_done
_imp_done = False
# Test _imp_done

# code_ok
code_ok = False
# Test code_ok

# Module code
# Testing module code
"""
Constructor for code objects.
"""
__all__ = []

# Test all
# Test __all__

# Test _
_ = None
# Test _

# Test module docstring
__doc__ = None
# Test __doc__

# Test module name
__name__ = None
# Test __name__

# Test module file name
__file__ = None
# Test __file__

# Test module package
__package__ = None
# Test __package__

# Test future imports
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
# Test future imports

# Test nested scopes
x = 1
def f():
	print(x)
	x = 2
# Test nested scopes

# Test generator expressions
