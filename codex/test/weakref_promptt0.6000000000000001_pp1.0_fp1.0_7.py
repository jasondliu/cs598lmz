import weakref
# Test weakref.ref with a collection module and a custom class
from collections import deque
from weakref import ref
from test import support
from test.support.script_helper import assert_python_ok
import unittest
import gc
from collections import UserDict
from collections import UserList
from collections import UserString
import types
import sys
import pickle
import io
from test.support import import_module
from test.support.script_helper import assert_python_failure
from test.support.script_helper import assert_python_ok
import operator
import pickle
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
from collections import ChainMap
from collections import Counter
import re
from collections import UserList
from collections import UserDict
from collections import UserString
from collections import Counter
from collections import defaultdict
from collections import deque
from collections import UserList
from collections import UserDict
from collections import UserString
from collections import ChainMap
from collections import OrderedDict
from collections import Counter
from collections import defaultdict
