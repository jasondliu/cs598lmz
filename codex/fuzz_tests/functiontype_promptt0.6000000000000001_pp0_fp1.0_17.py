import types
# Test types.FunctionType

def test_function(level=1):
    if level > 10:
        return
    print("level: ", level)
    test_function(level+1)

print(type(test_function))
print(type(test_function(1)))


# Test types.LambdaType

#def test_lambda(level=1):
#    if level > 10:
#        return
#    print("level: ", level)
#    test_lambda(level+1)

#print(type(test_lambda))
#print(type(test_lambda(1)))

# Test types.GeneratorType

def test_generator(level=1):
    if level > 10:
        return
    print("level: ", level)
    yield level
    yield from test_generator(level+1)

print(type(test_generator))
print(type(test_generator(1)))
for i in test_generator(1):
    print(i)
