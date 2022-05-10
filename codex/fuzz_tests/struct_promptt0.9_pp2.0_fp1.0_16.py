import _struct
# Test _struct.Struct.
import struct
from struct import calcsize
struct_iterator = struct.__dict__.items()

for name, obj in struct_iterator:
    if name.startswith('Struct'):
        cls = type('_' + name, (_struct.Struct,), {})
        print('testing %s.format' % name)
        assert obj.format == cls(obj.format).format

        print('testing "%s"' % obj.format)
        print('struct size:', calcsize(obj.format))
        s = cls(obj.format)
        assert s.size == calcsize(obj.format)

        print('packing/unpacking:', end=' ')
        ns = []
        for n in range(s.size):
            ns.append(n)

        try:
            buf = s.pack(*ns)
        except struct.error as e:
            print(e)
            continue

        print('ok')
        print('packed string: %r' % (buf,))
        print('unpacking:', end=' ')

        try
