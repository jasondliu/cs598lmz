from _struct import Struct
s = Struct.__new__(Struct)
 
# If you want to build a struct with a particular name,
# you may need to cheat a bit:
 
import _struct
n = 'ABC'
Struct._name = n
Struct._struct_format = 's'
_struct._clearcache()
 
# Now, the Struct.__new__ will return a struct with name
# 'ABC' instead of the default 'struct'.
 
ABC = Struct.__new__(Struct)
 
# This will output "ABC"
ABC.__name__
 
# Just remember to clear the name after you're done, or
# further instances will inherit the name.
 
Struct._name = 'struct'
 
# Real world example using all that
 
import sys
args = sys.argv[1:]  # sys.argv[0] is the script name.
                             
if not args:
    print('Usage: {} N1 N2 N3'.format(sys.argv[0]))
else:
    numbers = list(map(int, args))
