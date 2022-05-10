gi = (i for i in ())
# Test gi.gi_code: it should be the function object (f).
print(gi.gi_code is f)


# Check the initialisation of the gi_frame.
def f():
    gi = (i for i in ())
    print(gi.gi_frame.f_locals)


f()


# Check the initialisation of the gi_frame.
def f():
    gi = (i for i in ())
    print(gi.gi_frame.f_locals)


f()


# Check the initialisation of the gi_frame.
def f():
    gi = (i for i in ())
    print(gi.gi_frame.f_locals)


f()


def f():
    gi = (i for i in ())
    print(gi.gi_frame.f_locals)


f()


def f():
    gi = (i for i in ())
    print(gi.gi_frame.f_locals)


f()

# Check the initialisation of the gi_frame.
def f():
   
