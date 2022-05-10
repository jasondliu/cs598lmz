import _struct

def get_timestamp():
    return strftime("%Y-%m-%d %H:%M:%S",  gmtime())

def get_delta(end, start):
    """how many seconds have elapsed between start and end?"""
    if(start == None):
        start = datetime.datetime.now()
    delta = (end - start)
    return delta.days * 24 * 60 * 60 + delta.seconds + float(delta.microseconds) / 1000000

def get_elapsed(delta):
    """given a number of seconds, return a string of form [XmYYs]"""
    if(delta == None):
        raise ValueError("delta is None")
    if(delta < 0):
        raise ValueError("delta must be >= 0")
    minutes = int(delta/60)
    seconds = delta - 60 * minutes
    result = ""
    if(minutes > 0):
        result += "%dm" % minutes
    result += "%.3fs" % seconds
    return result

