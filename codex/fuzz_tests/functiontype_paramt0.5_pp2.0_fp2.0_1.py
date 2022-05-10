from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

#Sorted
list.sort()
sorted(list)

#Reversed
list.reverse()
reversed(list)

#Map
map(None, list)

#Filter
filter(None, list)

#Reduce
reduce(None, list)

#Enumerate
enumerate(list)

#Zip
zip(list)

#All
all(list)

#Any
any(list)

#Max
max(list)

#Min
min(list)

#Sum
sum(list)

#Len
len(list)

#Abs
abs(value)

#Round
round(value)

#Int
int(value)

#Float
float(value)

#Bool
bool(value)

#Str
str(value)

#Chr
chr(value)

#
