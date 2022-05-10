fn = lambda: None
# Test fn.__code__.co_filename
print fn.__code__.co_filename

# Test os.path.realpath()
print os.path.realpath(__file__)

# Test os.path.abspath()
print os.path.abspath(__file__)

# Test os.path.dirname()
print os.path.dirname(__file__)

# Test os.path.relpath()
print os.path.relpath(os.path.dirname(__file__))

# Test os.path.relpath()
print os.path.relpath(__file__)

# Test os.path.basename()
print os.path.basename(__file__)

# Test inspect.getfile()
print inspect.getfile(lambda: None)

# Test sys.argv[0]
print sys.argv[0]

# Test os.path.abspath(os.path.dirname(sys.argv[0]))
print os.path.abspath(os.path.dirname(sys.arg
