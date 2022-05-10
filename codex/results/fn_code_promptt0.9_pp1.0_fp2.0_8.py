fn = lambda: None
# Test fn.__code__.co_files_paths
readpaths(fn, [__file__])
readpaths(fn, [])

# Test method.__code__.co_files_paths
def fn():
    class A:
        def method(self):
            pass

readpaths(fn.__code__, [__file__])
readpaths(fn.__code__, [])

# Do some tests against builtin modules
def fn():
    x = list()

# Test fn.__code__.co_files_paths
readpaths(fn, [])

# Test some builtin types
def fn():
    x = list()
    x > 3

# Test fn.__code__.co_files_paths
readpaths(fn, [])

# Test some builtin types
def fn():
    x = list()
    x.append(1)

# 
