from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import time
now = time.time()
now

now = time.ctime(now)
now

time.gmtime(now)

time.localtime(now)

time.mktime(time.localtime(now))

time.strftime("%m/%d/%Y %H:%M", time.localtime(now))

time.strptime("30/12/2009", "%d/%m/%Y")

import datetime
d = datetime.date.today()
d

d.year

d.month

d.day

d.ctime()

d.isoweekday()

d.isoformat()

d.strftime("%d/%m/%Y")

d.strptime("30/12/2009", "%d/%m/%Y")

d.replace(year=2010)

