import _struct
# Test _struct.Struct objects with forbidden names, such as 'type'.

try:
    print(_struct.Struct('b'))
except TypeError as msg:
    print(msg)

try:
    print(_struct.Struct(b'b'))
except TypeError as msg:
    print(msg)

try:
    print(_struct.Struct(1))
except TypeError as msg:
    print(msg)

try:
    print(_struct.Struct('<'))
except TypeError as msg:
    print(msg)
