from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

from time import localtime

now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)

from time import mktime, strptime
time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print(utc_now)

from datetime import datetime
now = datetime(2014, 8, 10, 18, 18, 30)
now_str = now.strftime(time_format)
print(now_str)

from datetime import datetime
time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
print(now)

from datetime import timedelta
a = timedelta(days=2, hours
