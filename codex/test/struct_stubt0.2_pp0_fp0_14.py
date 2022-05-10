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

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))

time.strptime('2013-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')

import calendar
calendar.isleap(2013)

calendar.isleap(2012)

calendar.month(2013, 12)

calendar.month(2013, 12, w=2, l=1)

calendar.calendar(2013)

calendar.weekday(2013, 12, 31)

calendar.weekday(2013, 12, 31)
