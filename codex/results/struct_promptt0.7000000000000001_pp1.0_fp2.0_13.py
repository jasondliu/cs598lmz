import _struct
# Test _struct.Struct, _struct.error and _struct.calcsize().
import sys

def test_struct():
    # Test _struct.Struct object.
    import sys
    s = _struct.Struct('hhl')
    for spec, obj in ('hhl', s), ('=hhl', s):
        print('Testing _struct.Struct(%r)' % (spec,))
        print('obj=%r, obj.__class__=%r' % (obj, obj.__class__))
        print('obj.format=%r, obj.size=%r, obj.alignment=%r'
              % (obj.format, obj.size, obj.alignment))
        if obj.format != spec[-1] or obj.size != s.size:
            raise ValueError('__init__ failed')
        # Retrieve specs from struct object.
        format2 = obj.format
        size2 = obj.size
        alignment2 = obj.alignment
        if format2 != spec[-1] or size2 != s.size:
            raise ValueError('attribute retrieval failed')
       
