import types
# Test types.FunctionType
def f(): pass
def g(): pass
def h(): pass
def i(): pass
def j(): pass
def k(): pass
def l(): pass

def test_function(f):
    if isinstance(f, types.FunctionType):
        return f()

def test_function_call(f):
    return f()

print(test_function(f))
print(test_function(g))
print(test_function(h))
print(test_function(i))
print(test_function(j))
print(test_function(k))
print(test_function(l))
print(test_function_call(f))
print(test_function_call(g))
print(test_function_call(h))
print(test_function_call(i))
print(test_function_call(j))
print(test_function_call(k))
print(test_function_call(l))
