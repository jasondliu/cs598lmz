import types
types.MethodType(lambda self, x: x, None)

# Issue #22
# The following code should not raise an exception
import types
types.MethodType(lambda self, x: x, None, None)

# Issue #23
# The following code should not raise an exception
import types
types.MethodType(lambda self, x: x, None, None, None)

# Issue #24
# The following code should not raise an exception
import types
types.MethodType(lambda self, x: x, None, None, None, None)

# Issue #25
# The following code should not raise an exception
import types
types.MethodType(lambda self, x: x, None, None, None, None, None)

# Issue #26
# The following code should not raise an exception
import types
types.MethodType(lambda self, x: x, None, None, None, None, None, None)

# Issue #27
# The following code should not raise an exception
import types
