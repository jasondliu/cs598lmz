import types
# Test types.FunctionType: currently requires a nodefunctor
# TODO: implement a more generic typecheck
def f(a):
    def df(b):
        return b + a
    return df
a = np.array([1,1,1,1])
assert isinstance(f(a),types.FunctionType)

def g(a):
    return np.array([1,1,1,1])

assert not isinstance(g(a),types.FunctionType)

# Test lift
def h(a,b):
    return a + b

assert lift(h)([np.array([1,1,1,1]),np.array([1,1,1,1])])[0] == 2

# Test Match
m = Match(a,2)

# Test Match.eq and Match.neq
assert m.eq(a).all() 

# Test Match.between
assert m.between(1,3).all()

# Test Match.contains
assert m.contains([1,1,1]).all()

# Test Match.less
assert m
