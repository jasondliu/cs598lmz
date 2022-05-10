fn = lambda: None
# Test fn.__code__.__sizeof__()
fn.__code__.__sizeof__  # [sizeof]

# Test inspect.findsource() called on dynamically generated code.
findsource_code = """
def fn(foo, bar, baz=1, *, qux=(), **kwargs):
    if not qux:
        return foo*bar*baz
    return abs(pow(getattr(foo, 'x', foo), qux))
"""

findsource_code_compiled = compile(findsource_code, '<findsource>',
                                   'exec', ast.PyCF_ONLY_AST)
findsource_code_exec = compile(findsource_code_compiled, '<findsource>',
                               'exec')
exec(findsource_code_exec)
# Test inspect.findsource()
inspect.findsource(fn)

# Test inspect.getargs().
inspect.getargs(fn.__code__)

# Test inspect.getsourcelines().
inspect.getsourcelines(fn)

# Test inspect.joinseq().

