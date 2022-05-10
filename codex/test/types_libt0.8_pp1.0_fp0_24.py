import types
types.ClassType

#Old style exceptions
class MyError(StandardError):
    pass

#New style exception
class MyError(Exception):
    pass

#raise exceptions
class MyError(Exception):
    def __str__(self):
        return 'here my custom error message'

try:
    raise MyError
except MyError as e:
    print('Got this error: ' + str(e))


def safe_division(number, divisor, ignore_overflow,
                   ignore_zero_divison):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_divison:
            return float('inf')
        else:
            raise

#TODO
#__enter__, __exit__

#Files

#f = open('my_file.txt')
#f.name
#f.mode
#f.close()

