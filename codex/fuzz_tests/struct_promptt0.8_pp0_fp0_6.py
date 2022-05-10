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
for prefix in ('@', '<', '>', '=', '!'):
    for format in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'n', 'N',
        'f', 'd'):
        for size in (0, 1, 2, 3, 4, 5, 10):
            for postfix in struct_tests:
                full_format = prefix + str(size) + format +
