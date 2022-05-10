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

time.asctime(time.localtime(now))

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))

time.strptime('2015-06-29 18:19:20', '%Y-%m-%d %H:%M:%S')

import calendar
calendar.isleap(2015)

calendar.isleap(2016)

calendar.month(2015, 6)

calendar.monthcalendar(2015, 6)

calendar.calendar(2015)

import os
os.getcwd()

os.chdir('/Users/michael')

