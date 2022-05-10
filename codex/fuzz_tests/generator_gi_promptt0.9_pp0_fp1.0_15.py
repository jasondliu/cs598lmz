gi = (i for i in ())
# Test gi.gi_code
gi.gi_code  # This is not valid on 3.2+
# Test gi.gi_frame
gi.gi_frame  # This is not valid on 3.2+
# Test gi.gi_running
gi.gi_running  # This is not valid on 3.2+
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.yeild()
sent = gi.send(1)

# Test GeneratorExit
with raises_exc(TypeError):
    gi.throw(GeneratorExit)

# Test function attributes
def f():
    """this is a function"""
    pass

f.attr1 = 1
f.attr2 = "str"
f.attr3 = []
f.attr4 = (1, 2, 3)  # compute-around object

# Test attrs of builtin functions
len.attr1 = 1
len.attr2 = "str"
len.attr3 = []
len.attr4 = (1, 2, 3)  # compute-around object


def f():

