import ctypes
ctypes.cast(1337, ctypes.py_object)

True
type(True)

False
type(False)

None
type(None)

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

a, b, c = 1, 1.5, 'hello'

dates = [1979, 1980, 1981, 1982, 1983, 1984]
dates[0]
#dates[::2]

# Dates : 1979 ~ 1984
['{0}년'.format(i) for i in dates]

date_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

for i in sorted(date_dict.keys()):
    print(i, date_dict[i])

'a' in date_dict
