fn = lambda: None
# Test fn.__code__

# Test a long traceback
def fn_a():
    def fn_b():
        def fn_c():
            def fn_d():
                def fn_e():
                    def fn_f():
                        def fn_g():
                            def fn_h():
                                def fn_i():
                                    def fn_j():
                                        def fn_k():
                                            def fn_l():
                                                x = 1/0
        return 42 + 42
    return 42 + 42

print( sys.exc_info() )

if sys.version_info[0] == 2:
    # PY2 has exec
    def fn2():
        exec("foo=1")
else:
    # Compile bc Py3 eval can't handle non-string literal
    c = compile("foo=1", "fname", "exec")
    def fn2():
        exec(c)

# Test a high-recursion chain
def high_recursion():
    return high_recursion()

def some_decorator(f):
    return f
