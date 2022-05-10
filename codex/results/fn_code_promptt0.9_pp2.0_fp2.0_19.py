fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', None)
# Test fn.__closure__
setattr(fn, '__closure__', None)
# Test fn.__globals__
setattr(fn, '__globals__', None)
# Test fn.func_defaults
# setattr(fn, 'func_defaults', None)


# Test types.CodeType
test_CodeType = []
test_CodeType.append((None, None, None, None, None, None, None, None, None, None, None, None, None))
test_CodeType.append(('', '', '', '', '', '', '', '', '', '', '', '', ''))
test_CodeType.append((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
test_CodeType.append(('asdf', 1, None, {}, [], '', [], 0, True, False, (), (4, 5), {}))

@check_exception(NameError)
def test_create_
