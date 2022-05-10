import signal
# Test signal.setitimer
X.append(signal.setitimer(signal.ITIMER_VIRTUAL,10,2))

# Check length of X.
X.append(len(X))

# Check the module name.
X.append(signal.__name__)



# Check name of globals and argv
import sys
X.append(['argv' in sys.__dict__])
X.append(['path' in sys.__dict__])
X.append(['meta_path' in sys.__dict__])
X.append(['modules' in sys.__dict__])




# Test sys.settrace, sys.setprofile, sys.exc_info()
def foo():
    X.append('in foo()')
sys.settrace(foo)

def bar():
    raise Exception()
    # trace function should not be called if
    # exception not raised
    X.append('in bar()')

try:
    bar()
except:
    pass

# Check exc_info()
X.append(sys.exc_info())


