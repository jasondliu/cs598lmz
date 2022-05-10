fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Issue #26205: refleaks in pydoc.
import pydoc
import sys
pydoc.Helper(sys.stdout)

# Issue #26230: refleaks in the trace module.
import trace
trace.trace(trace=True, count=True)

# Issue #26231: refleaks in the inspect module.
import inspect
inspect.getfile(inspect)

# Issue #26232: refleaks in the tokenize module.
import tokenize
tokenize.tokenize(b'0')

# Issue #26233: refleaks in the dis module.
import dis
dis.dis(lambda: None)

# Issue #26234: refleaks in the parser module.
import parser
parser.expr('0')

# Issue #26235: refleaks in the symbol module.
import symbol
symbol.sym_name[0]

# Issue #26236: refleaks in the keyword module.
import keyword
keyword.iskeyword('for')

# Issue #26237: refleaks in
