fn = lambda: None
# Test fn.__code__.co_filename is None
x = fn.__code__.co_filename

# Test fn's __globals__ is a dict
x = fn.__globals__
# I don't know how to test to see if fn's __globals__ has kwargs
#x = fn.__defaults__

# Test for sys module
# I don't know how to test to see if sys's __globals__ has kwargs
import sys
x = sys.__globals__
#x = sys.__defaults__

# Test for sys.exit
sys.exit()

# Test for sys.argv
x = sys.argv

# Test for sys.argv[0]
x = sys.argv[0]

# Test for sys.argv[1]
x = sys.argv[1]

# Test for sys.argv[2]
x = sys.argv[2]

# Test for sys.argv[3]
x = sys.argv[3]

# Test for sys.argv[
