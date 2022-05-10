import _struct
import _thread
import _time
import _weakref
import _weakrefset
import _warnings
import _weakref

# The _operator module is imported first, because this module is
# implicitly imported by some code that checks for None.
import _operator

# The _collections module is imported next, because it defines
# the defaultdict class, and the OrderedDict class is used by some
# code that checks for None.
import _collections

# The _functools module is imported next, because it defines the
# partial class, and the partial class is used by some code that
# checks for None.
import _functools

# The _random module is imported next, because it defines the
# random class, and the random class is used by some code that
# checks for None.
import _random

# The _heapq module is imported next, because it defines the
# heapq class, and the heapq class is used by some code that
# checks for None.
import _heapq

# The _bisect module is imported next, because it defines the
# bis
