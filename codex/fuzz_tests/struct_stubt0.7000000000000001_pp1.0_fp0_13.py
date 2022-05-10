from _struct import Struct
s = Struct.__new__(Struct)
print(s)
s.__init__('>f')
print(s)

s = Struct('>f')
print(s)

s.__init__('>f')
print(s)


#
# Method
#

print('\n#\n# Method\n#')

#
# Imported module
#

print('\n#\n# Imported module\n#')

import datetime

print(datetime.datetime)
print(datetime.datetime.__new__)

datetime.datetime.__new__(datetime.datetime, year=2015, month=12, day=1)

print(datetime.datetime.__new__(datetime.datetime, year=2015, month=12, day=1))

print(datetime.datetime.__new__(datetime.datetime, year=2015))

print(datetime.datetime.__new__(datetime.datetime))

print(datetime.datetime.__new__(datetime.datetime, year
