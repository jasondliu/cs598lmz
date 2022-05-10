import types
# Test types.FunctionType and types.UnboundMethod
def function(arg1=1, arg2=2, arg3=3):
    print arg1, arg2, arg3

def method(self, arg1=1, arg2=2, arg3=3):
    print self, arg1, arg2, arg3

class C:
    def method(self, arg1=1, arg2=2, arg3=3):
        print self, arg1, arg2, arg3

class D: pass

f_expected_values = [
    None,
    (1,),
    (1, 2),
    (1, 2, 3),
    (1, 2, 3, 4),
    (1, 2, 3, 4, 5),
    (1, 2, 3, 4, 5, 6),
    (1, 2, 3, 4, 5, 6, 7),
    (1, 2, 3, 4, 5, 6, 7, 8),
    (1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 2,
