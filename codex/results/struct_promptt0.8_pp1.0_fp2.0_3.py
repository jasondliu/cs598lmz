import _struct
# Test _struct.Struct with format letters from all groups.

# control string:  "=bBhHiIlLqQfdPxXeEgGcnSszZ0()|?{}"

import _struct

# This is a control string with all format letters
control = "=bBhHiIlLqQfdPxXeEgGcnSszZ0()|?{}"

def check(fmt, value):
    try:
        st = _struct.Struct(fmt)
    except (TypeError, _struct.error), e:
        print "exception: ", e
    else:
        packed = st.pack(value)
        unpacked = st.unpack(packed)
        print "in:%s out:%s" % (value, unpacked)
        if unpacked != (value,):
            print "ERROR: returned packed string does not roundtrip"

check(control, (1,)*len(control))
check(control, (0,)*len(control))
check(control, (255,)*len(control))

# values that
