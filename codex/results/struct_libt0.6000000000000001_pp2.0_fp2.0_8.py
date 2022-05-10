import _struct
import _sqlite3

from _sqlite3 import *

# Convenience: a datetime can be passed as a string to the adapt() function,
# and this will generate the appropriate converter function.
def adapt_datetime(val):
    return val.isoformat()

register_adapter(datetime.datetime, adapt_datetime)

# Convenience: a date can be passed as a string to the adapt() function,
# and this will generate the appropriate converter function.
def adapt_date(val):
    return val.isoformat()

register_adapter(datetime.date, adapt_date)

# Convenience: a time can be passed as a string to the adapt() function,
# and this will generate the appropriate converter function.
def adapt_time(val):
    return val.isoformat()

register_adapter(datetime.time, adapt_time)

# Register the adapter for datetime.datetime objects.
# This is required for the SQLite Date and Time Functions:
# http://www.sqlite.org/lang_datefunc.
