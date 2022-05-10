import types
types.MethodType(str, object)

# help or __doc__ or ?
dir(object())
dir(object)
dir('ascii')
dir(int)
dir(int(8))
int(8)
chr(65)
ord('A')
dir(bool)
c = complex(2,6)
dir(c)
# get the value of something
c.real
c.imag
f = float(1.0)
dir(f)
f.is_integer()
f = float('inf')
f.is_integer()
f = float('nan')
f.is_integer()
f.hex()
f = float('inf')
f.hex()
f.is_integer()
f.hex()
f.is_integer()

# set the value of something
c.real = 5
c.imag = 7

# exceptions
try:
    eval('''''')
except Exception as err:
    print("err: {}".format(err))

# exceptions looper
try:
    ''' create failure '''
except TypeError as
