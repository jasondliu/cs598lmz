from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__.items())

# 2
import sys
list(sys.modules.items())

# 3
import re
list(re.__dict__.items())

# 4
import json
list(json.__dict__.items())

# 5
import builtins
list(dir(builtins))

# 6
import __main__
list(__main__.__dict__.items())

# 7
import __builtin__
list(__builtin__.__dict__.items())

# 8
import __future__
list(__future__.__dict__.items())

# 9
import __builtins__
list(__builtins__.__dict__.items())

# 10
import copy
list(copy.__dict__.items())

# 11
import pprint
list(pprint.__dict__.items())

# 12
import collections
list(collections.__dict__.items())

# 13
import functools
list(functools.__dict__.items())


