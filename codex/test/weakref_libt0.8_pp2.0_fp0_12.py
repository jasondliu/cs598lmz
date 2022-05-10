import weakref
from icalendar import Calendar, Event
import redis


def cmp(a, b):
    return (a > b) - (a < b)

def cmp_by(a, b, key):
    return cmp(key(a), key(b))

def cmp_by_prop(a, b, propname):
    return cmp(getattr(a, propname), getattr(b, propname))

def cmp_by_key(a, b, key):
    return cmp(a[key], b[key])

def get_local_time(dt):
    """
        Return a timezone aware datetime object that associates the passed
        datetime with the local time zone. If the datetime object already has
        a time zone association, it is transformed to the local time zone.
    """
    tzname = time.tzname[time.daylight]
    tz = pytz.timezone(tzname)
    if tzname == 'GMT':
        tzname = 'UTC'
