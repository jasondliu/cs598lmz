fn = lambda: None
# Test fn.__code__.co_filename
params = len(sys.argv)
# Test fn.__code__.co_firstlineno
# Use os.path.basename() to test importing that module
v = os.path.basename(sys.argv[0])
# Test fn.__code__.co_lnotab, the line number and offsets
# Use os.path.dirname() to test importing that module
v = os.path.dirname(__file__)
v = os.path.relpath(__file__, "..")

# Test fn.__code__.co_code
if params == 1:
    # Test fn.__code__.co_varnames
    b = False
elif params == 2:
    # Test fn.__code__.co_nlocals
    b = True
else:
    # Test fn.__code__.co_stacksize
    b = False

# Test fn.__code__.co_names
print(b)

s = set()
# Test set.__init__
# Test set's constrains
