from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s = Struct('I 2s f')
s.size

import time
now = time.time()
print(now)
print(time.ctime(now))

print(time.gmtime(now))

print(time.localtime(now))

print(time.mktime(time.localtime(now)))

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))

print(time.strptime('2018-11-28 15:58:37', '%Y-%m-%d %H:%M:%S'))

import calendar
print(calendar.isleap(2018))

print(calendar.isleap(2020))

print(calendar.month(2018, 11))

print(calendar.monthcalendar(2018, 11))

print(calendar.calendar(2018))

print(calendar.weekday(2018, 11, 28))

print(
