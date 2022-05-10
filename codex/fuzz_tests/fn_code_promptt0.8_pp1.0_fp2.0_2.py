fn = lambda: None
# Test fn.__code__ is a code object
test_fn.__code__
# Test code object is not empty (more than just code object header)
assert(test_fn.__code__.__sizeof__() > sizeof(test_fn.__code__))
# Test code object has some bytecode
assert(len(test_fn.__code__.co_code) > 0)
from IPython.display import IFrame, display
from IPython.display import HTML

def show_assembly(fn):
    fn_name = fn.__name__
    try:
        HTML('<iframe src=http://web.eecs.utk.edu/~huangj/cs360/360/specs/single-file/{}.html width=1000 height=250></iframe>'.format(fn_name))
    except:
        print("Sorry, something went wrong.\nAre you connected to the Internet?\nIf you are, please let the instructor know.")
        print("In the meantime, here is the function name: {}".format(fn_name))
 
show_assembly(test_fn)
from IP
