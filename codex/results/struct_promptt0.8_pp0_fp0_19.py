import _struct
# Test _struct.Struct() and its methods.
STFORM1 = 'hhl'
STSIZE1 = _struct.calcsize(STFORM1)
ST1 = _struct.Struct(STFORM1)
STFORM2 = 'hhhhi'
STSIZE2 = _struct.calcsize(STFORM2)
ST2 = _struct.Struct(STFORM2)
S = ST1.pack(*(0, 1, 2 ** 31 - 1)) * 2
S += ST2.pack(*(0, 32767, 32767, 32767, 2 ** 31 - 1)) * 2
for st in ST1, ST2:
    print(st.unpack(S))
    st.unpack_from(S, 0)
    st.unpack_from(S, STSIZE1)
    st.unpack_from(S, len(S) - STSIZE2)

# Test _struct.iter_unpack().
for s_unpack in _struct.iter_unpack(STFORM1, S):
    print(type(s_unpack), s_unpack)
    print(list(s_
