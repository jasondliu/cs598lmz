fn = lambda: None
# Test fn.__code__ with a callable created with a lambda.
fn.__code__ = (lambda: None).__code__

# Test fn.__code__ with a callable created with the exec builtin,
# without specifying a globals or locals dict.
code1 = 'def fn(): 1\n'
co1 = compile(code1, '<string>', 'exec')
exec(co1)
fn.__code__ = fn.__code__

# Test fn.__code__ with a callable created with the exec builtin,
# specifying a globals dict, but no locals dict.
code2 = 'def fn(): 1\n'
co2 = compile(code2, '<string>', 'exec')
namespace = {}
exec(co2, namespace)
fn = namespace['fn']
fn.__code__ = fn.__code__

# Test name, filename, firstlineno, lnotab with a callable created
# with the exec builtin.
code3 = 'def fn(): 1\n'
co3 = compile(code3, '<string>', 'exec')
names
