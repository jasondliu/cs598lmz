import threading
threading.stack_size(32768)

def threading_function(arg):
    global result
    result = arg()

def async_call(arg_function, callback=None):
    global result
    result = None
    thread = threading.Thread(target=threading_function, args=(arg_function,))
    thread.start()
    thread.join()
    return result


# The following class was taken from
# http://code.activestate.com/recipes/576694/
# and modified.
# TwoTowTruck: an iterator that returns elements from two nested iterators
# in a round-robin fashion. Example:
# for x in TwoTowTruck([[1,2,3],[4,5,6]):
#      print x

class TwoTowTruck(object):
    """TwoTowTruck: an iterator that returns elements from two nested iterators
    in a round-robin fashion. Example:
    for x in TwoTowTruck([[1,2,3],[4,5,6]]):
         print x

