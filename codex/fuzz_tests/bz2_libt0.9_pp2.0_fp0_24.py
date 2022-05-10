import bz2
bz2.test()
print()

# https://docs.python.org/3/library/copy.html#module-copy
import copy
a = [1, 2, 3]
b = copy.copy(a)
b.append(4)
a
b
a = copy.deepcopy(b)
a
b

# https://docs.python.org/3/library/datetime.html#module-datetime
import datetime
datetime.date.today()
datetime.datetime.now()
datetime.datetime(2000,1,1)
datetime.datetime(2000,1,31,23,59,59,999999)
datetime.datetime(9999,12,31,23,59,59,999999)
datetime.datetime(2003,4,4,5,5,5,5).isoformat()
print()

# https://docs.python.org/3/library/enum.html
import enum
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

Color.RED
