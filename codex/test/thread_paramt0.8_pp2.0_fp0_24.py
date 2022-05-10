import sys, threading
threading.Thread(target=lambda:sys.stdout.write('mythread ran')).start()

# globbing/regular expressions
import glob
for name in glob.glob('dir/*[0-9].*'):
    print(name)

# and much more
# https://docs.python.org/2/library/

# HANDS-ON EXERCISE:
#  raw_input, time, datetime, calendar
#
# import the time module, get current time and print it out
import time
current_time = time.time()
print(current_time)
print('type(current_time) is', type(current_time))

# import the datetime module, get current date and print it out
import datetime
current_date = datetime.datetime.now()
print(current_date)
print('type(current_date) is', type(current_date))

# import the calendar module and use it to print out a calendar for the current month
import calendar
calendar.prmonth(current_date.year, current_date.month)

# Copyright (c) 2014, Matt
