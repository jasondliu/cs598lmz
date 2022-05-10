gi = (i for i in ())
# Test gi.gi_code.co_flags
gi.gi_code.co_flags
gi.gi_code.co_flags == 1

def hello2(s):
    s = s + 10
    return s

# Make different versions from hello2.
def hello2i():
    hello2(1)
# Test hello2i.func_code.co_flags
hello2i.func_code.co_flags
hello2i.func_code.co_flags == 1
def hello2o():
    hello2(1)
# Test hello2o.func_code.co_flags
hello2o.func_code.co_flags
hello2o.func_code.co_flags == 0
def hello2n():
    hello2(1)
# Test hello2n.func_code.co_flags
hello2n.func_code.co_flags
hello2n.func_code.co_flags == 33

a, b, c = 1, 2, 3
def fcn(a, b, c):
    d, e, f = a, b, c
    g =
