from types import FunctionType
a = (x for x in [1])
if a:
    print ('A:', a, 'is a generator')
else:
    print ('A:', a, 'is not a generator')
a = FunctionType(lambda x: x+1,{})
print(a(2))

import calendar
print(sum(calendar.day_name.index(i) for i in [["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"][i] for i in map(int,input().split())]))

def circle_area(r):
    # Your code here:
    return round(math.pi*r**2, 2)

def factorial(n):
    return math.factorial(n)

def p_series(n):
    # Your code here:
    return round(sum([(1/i) for i in range(1, n+1)]), 2)

def decimal_to_binary(n):
    return bin(n)[2:]

def avg_length(*args):
    return round((
