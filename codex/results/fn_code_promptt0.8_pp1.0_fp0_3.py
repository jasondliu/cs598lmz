fn = lambda: None
# Test fn.__code__.co_varnames
# Should print the string 'x'
print(fn.__code__.co_varnames)

# Test fn.__code__.co_argcount
# Should print the number 1
print(fn.__code__.co_argcount)

def get_info(fn):
	return [fn.__code__.co_varnames, fn.__code__.co_argcount]

# Test get_info() with the above function
info = get_info(fn)
print(info[0])
print(info[1])
