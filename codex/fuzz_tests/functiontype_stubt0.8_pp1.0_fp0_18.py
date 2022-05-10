from types import FunctionType
a = (x for x in [1])
b = [7, 3]
c = {1: 0}
d = 1.2
e = FunctionType
f = "abc"
print(repr(a))
print(repr(b))
print(repr(c))
print(repr(d))
print(repr(e))
print(repr(f))

def tostr(obj, indent = 0): #indent means how many spaces
    ind = '    ' * indent
    if isinstance(obj, list):
        return '[\n' + ',\n'.join([ind + tostr(x, indent+1) for x in obj]) + '\n' + ind + ']'
    elif isinstance(obj, dict):
        return '{\n' + ',\n'.join([ind + repr(k) + ': ' + tostr(v, indent+1) for k,v in obj.items()]) + '\n' + ind + '}'
    else: return repr(obj)

print(tostr([1,2,[3,4,{5:6,
