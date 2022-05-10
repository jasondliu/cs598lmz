import types
types.ClassType

## 4. Comparing Class Objects ##

L = [1, 2, 3]
M = [1, 2, 3]
L == M

type(L) == type(M)

type(L) == list

type(L) == type(M)

## 5. Customizing Your Classes ##

class Time(object):
    pass

time1 = Time()
time1.hour = 11
time1.minute = 59
time1.second = 30

## 6. Comparing Objects of the Same Class ##

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

current_time = Time(9, 14, 30)
start_time = Time(8, 3, 22)

current_time.hour
start_time.hour
current_time.hour > start_time.hour

current_time.minute
start_time.minute
current_time.minute > start_time.minute

