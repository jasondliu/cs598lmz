import socket
socket.if_indextoname(1)

import pprint
pprint.pprint(socket.getaddrinfo('www.python.org', 'http'))

import sys
sys.getsizeof(10)
sys.getsizeof(10.1)
sys.getsizeof(10.0)
sys.getsizeof(10.00000000001)

import time
time.time()
time.localtime(time.time())
time.asctime(time.localtime(time.time()))

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

time.strptime('2013-7-1', '%Y-%m-%d')

import calendar
calendar.month(2013, 7)

calendar.monthcalendar(2013, 7)

calendar.calendar(2013)

import random
random.random()

random.choice([1, 2, 3, 4, 5])

random.sample([1, 2, 3, 4, 5], 2)

