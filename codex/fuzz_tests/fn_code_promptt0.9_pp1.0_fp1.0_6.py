fn = lambda: None
# Test fn.__code__.co_argcount == 0
# Test fn.__code__.co_flags & 0x08 == 0
# Test fn.__code__.co_cellvars, fn.__code__.co_freevars
# Test fn.__annotations__
# Test fn.__kwdefaults__

# Test CodeTracer()
ct = CodeTracer()
ct.trace_function(test_fn)
ret = test_fn()
repr(ret)
ct.stop()

# Test TraceString()
ts = CodeTracer().trace_string('print("Hello")')
ts.run()

# Test TraceTfunction()
ts = CodeTracer().trace_string('a = 1\nb = 2\n')
ts.run('test')

# Test TraceString with tracer that does not allow locals and only traces one line
ts = CodeTracer(filter_func=None, allow_locals=False, trace_count=1).trace_string('a = 1\nb = 2\na + b\n')
ts.run()
