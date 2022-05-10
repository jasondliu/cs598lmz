from types import FunctionType
list(FunctionType(f.__code__, globals(), 'foo'))
function(lambda n: n+1)
[(lambda n: n+1)(n) for n in range(10)]
function(lambda s: s)
s = 'good morning.'
function(lambda s: s)
function(lambda s: s)('good morning.')
function(lambda s: s)('good morning.', 'Hello.')
function(lambda s: s)('good morning.', 'Hello.')
function(lambda s: s)(s, 'haha.')
function(lambda r: r)(1)
function(lambda s: s)(('a', 'b', 'c', 'd', 'e'))
def function(f):
    try:
        print(f([1, 2, 3, 4]))
    except Exception as e:
        print(e)
function(lambda s: s)
function(lambda s: s[0])
def function(f):
    try:
        print(f(('a', 'b', 'c', 'd', 'e')))
    except Exception as e
