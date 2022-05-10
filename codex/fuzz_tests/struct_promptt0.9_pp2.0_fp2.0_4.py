import _struct
# Test _struct.Struct.pack
struct_format = "bii"
string_value = "bbb"
buf = _struct.Struct(struct_format).pack(string_value,5,334)
len(buf)
# Test arithmetic operations
12 + 23
x = "abcd"
y = x.upper()
x = 12
x = x + 2
def test1():
    x = 10
    y = 20
    x = x+y
    return x
input_value = 20
x = "abcd\n"
output = x.upper()
len(x)
print(x)
print(output)

# Test multiplication and division and return value
def mult_div_test(a):
    print(a*2)
    return a/2
z = mult_div_test(55)
z
# List comprehension
a = [10,11,12]
z = [x*x for x in a]
z
# Test more functions
def un_func(a,b):
    """This is a doc string"""
    return a + b
un_func(25,12
