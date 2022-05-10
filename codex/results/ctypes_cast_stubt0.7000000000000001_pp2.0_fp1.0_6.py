import ctypes
ctypes.cast(10, ctypes.c_int)

## L4:

## Task 4.4.4
class Time(object):
    """
    Represents the time of day.
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    
    def __repr__(self):
        return 'Time(%d, %d, %d)' % (self.hour, self.minute, self.second)

    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __add__(self,
