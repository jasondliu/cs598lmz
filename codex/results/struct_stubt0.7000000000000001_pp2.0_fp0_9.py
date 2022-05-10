from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda x: 4
print(s.size(1))

from math import sqrt
print(sqrt(4))

from datetime import timedelta
t1 = timedelta(weeks=2)
t2 = timedelta(days=4)
t3 = t1 + t2
print(t3)

from datetime import date
today = date.today()
print(today)

from time import time
now = time()
print(now)
