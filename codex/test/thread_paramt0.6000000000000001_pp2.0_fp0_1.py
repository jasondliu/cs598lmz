import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Threading\n')).start()

#Printing to the screen
print('Printing')

#Dates and Times
from datetime import datetime
now = datetime.now()
print(now)
print(now.year, now.month, now.day)

#String formating
print('%s/%s/%s' % (now.month, now.day, now.year))
print('%s:%s:%s' % (now.hour, now.minute, now.second))

#String formatting with strings
print('%s-%s-%s' % (now.month, now.day, now.year))

#Basic Arthimetic
print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)
print(5 ** 5)
print(5 % 5)

#Variable Assignments
car_name = 'Wiebe Mobile'
car_type = 'Tesla Model S'
car_cylinders = 8
car_mpg = 9000.
