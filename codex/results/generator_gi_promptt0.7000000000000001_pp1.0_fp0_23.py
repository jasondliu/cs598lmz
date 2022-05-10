gi = (i for i in ())
# Test gi.gi_code


class A:

    def __iter__(self):
        yield 1

try:
    for i in A():
        break
except NameError:
    print("NameError")

# Test gi_frame


def f():
    yield 1
    yield 2
    yield 3

fgi = f()

# Test gi_running

try:
    fgi.send(None)
except TypeError:
    print('TypeError')
