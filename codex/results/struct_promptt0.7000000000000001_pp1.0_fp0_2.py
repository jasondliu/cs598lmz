import _struct
# Test _struct.Struct.pack_into

def pack_into(st,offset,fmt,*args):
    st.pack_into(fmt,offset,*args)
    return st.get_data()

def unpack_from(st,offset,fmt):
    return st.unpack_from(fmt,offset)

def pack(fmt,*args):
    return _struct.Struct(fmt).pack(*args)

def unpack(fmt,*args):
    return _struct.Struct(fmt).unpack(*args)

def getbuffer(st):
    return st.get_buffer()

def getdata(st):
    return st.get_data()

def getlen(st):
    return st.get_length()

class TestStruct:

    def test_unpack(self):
        pack_into = _struct.Struct('hhl')
        st = pack_into.get_buffer()
        pack_into.pack_into('hhl',0,1,2,3)
        assert pack_into.unpack_from('
