import select
# Test select.select():
select.select([1, 2], [], [])

# Test random.sample():
import random
r = random.sample([1, 2, 3], 2)

def test_trace2():
    """Test tracing without line events"""
    f, filename = mktemp()
    f.write("""print 1
if 1:
    print 2
    a = 3
    b = a + 1
    print a, b
    a = [x for x in range(5)]
    print a
    b = {'x': 1, 'y': 2}
    print b
    if 1:
        print 3
        a = 4
        b = a + 1
    print a, b
    a = (x for x in range(5))
    print a
    print 4

import sys
sys.stdout.write("sys.stdout.write")
sys.stdout.flush()

import os
os.write(1, "os.write")

a = 5
a
""")
    f.close()
    try:
        data = tracerun
