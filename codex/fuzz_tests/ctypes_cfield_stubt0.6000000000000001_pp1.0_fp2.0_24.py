import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def write_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def test_field_as_ctypes_field(tmpdir):
    p = tmpdir.join('test.py')
    p.write('''
from __future__ import print_function
import ctypes
from _ctypes_test import S, write_to_file, ctypes

print(S.x)
print(type(S.x))
print(ctypes.CField)
print(type(S.x) is ctypes.CField)
write_to_file("test.out", str(type(S.x) is ctypes.CField))
''')
    out = tmpdir.join("test.out")
    assert subprocess.call([sys.executable, str(p)],
                           stdout=out.open("w")) == 0
    assert out.read() == "True"

def test_field_as_ctypes_field_nested(tmpdir):
    p = tmp
