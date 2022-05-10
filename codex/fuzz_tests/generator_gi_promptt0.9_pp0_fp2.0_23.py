gi = (i for i in ())
# Test gi.gi_code
gi.gi_code is type(gi.gi_code)()
# Test gi.__name__
gi.__name__ is type(gi.__name__)()
# Test gi.gi_name
gi.gi_name is type(gi.gi_name)()
# Test gi.gi_frame
gi.gi_frame is type(gi.gi_frame)()
# Test gi.gi_running
gi.gi_running is type(gi.gi_running)()
""")

run_test(__name__, '__main__', """\
# Make sure that the generator is not needed any more once an iterator is
# created.
gi()
assert gi.gi_code is type(gi.gi_code)()
""")

run_test(__name__, '__main__', """\
# Test sending None to the generator and the sending of StopIteration the the
# main generator loop.
def gen_fun():
    yield 1

gi = gen_fun()
assert gi.send(None) == 1
gi.close()

