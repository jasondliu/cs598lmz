fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

'''
Expected:
    <class 'TypeError'>
    <class 'TypeError'>
'''

print(type(__exception__))
print(__exception__.__class__)
print(str(__exception__))

'''
Output:
    <class 'TypeError'>
    <class 'TypeError'>
    code object expected
'''
