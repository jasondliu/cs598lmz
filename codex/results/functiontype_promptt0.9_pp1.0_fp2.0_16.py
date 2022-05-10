import types
# Test types.FunctionType
def TestFuncType():
    a = types.FunctionType(None, globals())
    if( a == None):
        print 'None = None, Not needing test'
    a = types.FunctionType(a, globals())
    if( a == None):
        print 'None = None, Not needing test'
    print a
    a = types.FunctionType(a, globals())
    if( a == None):
        print 'None = None, Not needing test'
    a = types.FunctionType(a, globals())
    if( a == None):
        print 'None = None, Not needing test'
    a = types.FunctionType(a, globals())
    if( a == None):
        print 'None = None, Not needing test'
    a = types.FunctionType(a, globals())
    if( a == None):
        print 'None = None, Not needing test'
    print a

# Main program
TestFuncType()
