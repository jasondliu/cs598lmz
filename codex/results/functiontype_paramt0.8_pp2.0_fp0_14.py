from types import FunctionType
list(FunctionType(lambda: 0, {}))

# Set

s = {1, 2}
s | {3, 4}  # Union
s & {3, 4}  # Intersection
s ^ {3, 4}  # Symmetric difference (XOR)
s - {3, 4}  # Difference
s + {3, 4}  # Unsupported (sum)

# Convert

a = set()
a.update([1, 2])
a.add(1)  # update or add, set is also like a dict with key/value pair,
          # but here key is value, so it will be ignored
a.remove(1)

# Special forms

# All

all([True, True, False])  # False
all([True, True])  # True
all([True, False])  # False
all([])  # True

# Any

any([True, True, False])  # True
any([True, True])  # True
any([True, False])  # True
any([])  # False

# Iterator

it = iter([
