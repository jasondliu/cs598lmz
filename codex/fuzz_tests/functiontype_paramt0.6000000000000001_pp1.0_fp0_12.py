from types import FunctionType
list(FunctionType(code, globals()))

# <codecell>

# This is the same as the above.
import numpy as np
np.array(map(lambda x: x**2, xrange(10)))

# <codecell>

# Here is the same thing, but with a more complex expression.
code = compile('[x**2 for x in xrange(10) if x % 2 == 0]', '', 'eval')
list(FunctionType(code, globals()))

# <codecell>

# And here is the equivalent expression using the numpy library.
import numpy as np
np.array(filter(lambda x: x % 2 == 0, map(lambda x: x**2, xrange(10))))

# <codecell>

# Here is a simple expression that uses a function.
code = compile('x(10)', '', 'eval')
list(FunctionType(code, globals()))

# <codecell>

# Here is the equivalent expression using the numpy library.
import numpy as np
np.array(map(lambda x
