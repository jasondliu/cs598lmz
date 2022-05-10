gi = (i for i in ())
# Test gi.gi_code is None.
print(gi.gi_code is None)
# Test that gi.gi_frame is None.
print(gi.gi_frame is None)
# One more test: __next__() should raise a StopIteration exception.
StopIteration
try:
    gi.__next__()
except:
    print("StopIteration exception was raised")

# The StopIteration exception may "inherit" arguments that is passed to
# the .throw() method.
def my_stop_iteration(v):
    raise StopIteration(v)

try:
    my_stop_iteration(5).throw()
except Exception as e:
    print("StopIteration exception raised, value is {}".format(e.value))


# Chain iterators
class ChainIterator(object):
    def __init__(self, iter1, iter2):
        self.iter1, self.iter2 = iter1, iter2
        self.current_iter = iter1

    def __iter__(self):
        return self

    def __next__(self):
       
