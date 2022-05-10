from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import time
now = time.time()
now

int(now)

now = 1407694710.516145
time.gmtime(now)

time.localtime(now)

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))

time.strptime('2014-08-18', '%Y-%m-%d')

time.mktime(time.strptime('2014-08-18', '%Y-%m-%d'))

import datetime
d = datetime.date(2014, 8, 18)
d

d.year

d.month

d.day

d.timetuple()

datetime.date.fromtimestamp(now)

datetime.date.today()

datetime.date.today().strftime('%Y-%m-%d')

d.strftime
