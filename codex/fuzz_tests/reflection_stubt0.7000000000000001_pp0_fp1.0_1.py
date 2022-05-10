fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

def f():
  return fn()

print(f())
'''),
    '''\
Traceback (most recent call last):
  File "<string>", line 15, in <module>
TypeError: 'code' object is not callable
'''))

TestCases.append((
    dict(
        desc='Function code object is not callable',
        input='''\
def f():
  return f.__code__()

print(f())
''',
        expect_exception=True),
    '''\
Traceback (most recent call last):
  File "<string>", line 3, in <module>
TypeError: 'code' object is not callable
'''))

TestCases.append((
    dict(
        desc='Function code object is not callable',
        input='''\
def f():
  return f.__code__()

print(f())
''',
        expect_exception=True,
        flags=['--experimental-code-coverage']),
    '''
