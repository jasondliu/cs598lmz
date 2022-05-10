import types
types.__name__

types.FileType

type(1)

type(1) == types.IntType

import sys
sys.__name__

sys.stdin
sys.stdout

sys.stderr

sys.stdout.write("hello, world\n")

sys.stdout.write("hello, world\n")

print "hello, world"

sys.stdin.readline()

sys.maxint

sys.maxint * sys.maxint

sys.maxint + 1

sys.maxint + 1

sys.maxint + 1


# turn a sequence of ints into a string
import string
string.join(map(str, (1, 2, 3, 4)))

# turn a sequence of ints into a string
import string
string.join(map(str, (1, 2, 3, 4)), ", ")

# turn a string into a list of ints
reduce(lambda x, y: x * 10 + y, map(int, "1234"), 0)

# turn a string
