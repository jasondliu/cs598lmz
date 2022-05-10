from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import time
now = time.time()
now

time.ctime(now)

time.gmtime(now)

time.localtime(now)

time.mktime(time.localtime(now))

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))

time.strptime('2018-01-01 12:00:00', '%Y-%m-%d %H:%M:%S')

time.timezone

time.tzname

time.altzone

time.daylight

time.localtime()

time.timezone, time.tzname

time.altzone, time.daylight

time.strftime('%z', time.localtime())

time.strftime('%Z', time.localtime())

time.strftime('%c', time.localtime())

time.strftime
