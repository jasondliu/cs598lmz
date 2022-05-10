import types
types.MethodType(lambda self: None, None, Dummy)

# do not import *
from types import *

# (don't check for if __name__ == "__main__":)
# assert False, "unreachable"
