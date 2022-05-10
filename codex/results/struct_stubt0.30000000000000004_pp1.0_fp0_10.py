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

time.ctime(1437746094.5735958)

time.gmtime(now)

time.localtime(now)

time.mktime(time.localtime(now))

time.asctime(time.localtime(now))

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))

time.strptime('2015-08-19 11:11:11', '%Y-%m-%d %H:%M:%S')

time.ctime()

time.sleep(1)

time.ctime()

time.process_time()

time.perf_counter()

time.perf_counter()

time.perf_counter()

time.perf_counter()

time.perf
