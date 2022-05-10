from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size
s.pack(b'123')

s.unpack(b'\x12\x34\x56\x78\x9A\xBCdefg')

# format string
'{:5d}'.format(10)
'{:05d}'.format(10)
'{:x}'.format(255)
'{:.2f}'.format(3.1415926535)
'{:b}'.format(11)
'{:#x}'.format(255)
'{:#o}'.format(10)

# datetime
import datetime
datetime.datetime.now()
datetime.datetime.now() + datetime.timedelta(days=1, hours=10)

# Timezones
import pytz
pytz.all_timezones
pytz.country_timezones['IN']
datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

# Parsing and formatting dates
import dateutil
