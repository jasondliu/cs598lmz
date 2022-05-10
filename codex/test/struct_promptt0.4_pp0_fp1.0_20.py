import _struct
# Test _struct.Struct with all native byte orders.
for byteorder in '@=<>!':
    st = _struct.Struct(byteorder + 'hhl')
    s = st.pack(1, 2, 3)
    print(st.unpack(s))

# Test _struct.Struct with all native byte orders and alignment.
for byteorder in '@=<>!':
    for alignment in [True, False]:
        st = _struct.Struct(byteorder + 'hhl', alignment)
        s = st.pack(1, 2, 3)
        print(st.unpack(s))

# Test _struct.Struct with all native byte orders, alignment and format.
for byteorder in '@=<>!':
    for alignment in [True, False]:
        for format in ['hhl', 'hhh', 'llh', 'hhhll', 'hhllh', 'hhlhh']:
            st = _struct.Struct(byteorder + format, alignment)
            s = st.pack(1, 2, 3, 4, 5, 6)
