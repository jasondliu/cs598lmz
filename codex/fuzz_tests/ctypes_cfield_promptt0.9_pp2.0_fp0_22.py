import ctypes
# Test ctypes.CField
CFIELD_TYPE = ctypes.CFUNCTYPE(
    # Type definitions of the callback function
    ctypes.c_long,
    ctypes.c_long,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
)
def c_func(playerID, eventID, tick, sec, min, hour, weekDay, monthDay, month, year):
    # Requirements for callback function
    print "playerID:", playerID
    print "eventID:", eventID
    print "tick:",tick
    print "sec:",sec
    print "min:",min
    print "hour:",hour
    print "weekDay:",weekDay
    print "monthDay:",monthDay
    print "month:",month
    print "year:",year
    # Function should return 0 if succeeded
    return 0
#
