gi = (i for i in ())
# Test gi.gi_code.co_code
locals()[getattr(type(gi), 'gi_code', 'co_code').co_name]

# load_module_dynamic()
import os
name = os.__name__
import sys
mod = sys.modules[name]
code = compile('x=1', 'dummy', 'single', 0, 1)
getattr(mod, '__spec__', mod).loader.exec_module(mod) # XXX eval_frame


## ---------- ##
## cmath_test ##
## ---------- ##

# Issue #21000
import cmath, _testcapi
cmath._test()
inf = float('inf')
_testcapi.test_complex()
del inf

# Test complex ** complex
cmath.exp(1j * cmath.pi)
cmath.exp(2j * cmath.pi)
(2j * cmath.pi) ** 0.5
cmath.polar(1j)  # check for __float__
(1.5+1j)*(1+2j) # see http://bugs
