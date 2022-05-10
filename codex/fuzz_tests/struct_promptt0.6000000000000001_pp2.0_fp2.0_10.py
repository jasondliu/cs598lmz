import _struct
# Test _struct.Struct

# Test that a single struct is used for all instances of a given format.

# This is not required by Python, but it is useful for performance.

# Note that we check for identity rather than equality.

import struct

# We use a format that has a single character.
# Using multiple characters would make the test too slow.
# Using a format that is not valid would make the test too hard to read.

fmt = 'c'

# The following code uses a large number of copies of a Struct object.
# We want to ensure that they all use the same memory.

# We use a large number of copies because we want to be sure that
# the memory is not released even when the original is no longer needed.

# We use a small number because we don't want the test to take too long.

n = 1000

# We use a list to ensure that the Struct objects are kept alive.

# We use a list rather than a set because we want to ensure that
# the Struct objects are not equal.

# We use a list rather than a tuple because we want to be able to
# add
