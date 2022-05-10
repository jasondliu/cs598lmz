import _struct
# Test _struct.Struct when a format string is passed.
# Unfortunately, the test can't be exhaustive: at the C level, it is not
# possible to probe whether a format string is valid.
import sys, struct, operator
from functools import reduce
from test.support import run_unittest, import_module, bigmemtest
from test import support
struct_tests = (
    ('x'), ('c', 'x'), ('cx'), ('xc'), ('s', 'x'), ('sx'), ('xs'), ('p', 'x'),
    ('px'), ('xp'), ('P', 'x'), ('Px'), ('xP'))
