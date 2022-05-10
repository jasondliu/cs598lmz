import types
types.ClassType
types.TypeType

# Subclasses
isinstance(3, int)
isinstance(3.6, int)
isinstance('abc', str)
isinstance([1, 2, 3], list)
isinstance(dict, object)
isinstance(list, object)



# Exception
try:
    1/0
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
except RuntimeError, e:
    print 'RuntimeError:', e
except Exception, e:
    print 'Exception:', e

# try .. except .. finally
try:
    1/0
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
except:
    print 'Exception:', e
else:
    print 'No exception'
finally:
    print 'finally'

# raise exception
try:
    raise Exception("Exception message here")
except Exception, e:
    print 'Exception:', e
try:
    raise Exception("Exception message here")
except Exception, e:
    print 'Exception:', e

