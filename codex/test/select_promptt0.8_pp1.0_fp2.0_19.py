import select
# Test select.select for:
# 1. Interrupted system call
# 2. Behavior when one of the descriptors is a bad integer (e.g. -1)
# 3. Behavior when one of the descriptors is too large (outside of range)
# 4. Behavior when too many descriptors are supplied

# Create a pipe
r, w = os.pipe()

def bad_integer():
    # Need an arbitrary large integer that won't be an open fd
    # on this system. This value works on Linux/Mac/Windows.
    # Arbitrary choice: 2^31
    return 2147483648

