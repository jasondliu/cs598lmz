import _struct
# Test _struct.Struct.size
for fmt in ['hhl', 'hhi', 'hhq', 'jjl', 'jiq', 'bl', 'bi', 'bq']:
    st = _struct.Struct(fmt)
    print(fmt, '->', st.size)

# Test struct.Struct.format
for fmt in ['hhl', 'hhi', 'hhq', 'jjl', 'jiq', 'bl', 'bi', 'bq']:
    st = _struct.Struct(fmt)
    print(repr(st.format))
    if fmt != st.format:
        d.err('{!r} != {!r}'.format(fmt, st.format))

# Test struct.Struct.pack()
for fmt in ['hhl', 'hhi', 'hhq', 'jjl', 'jiq', 'bl', 'bi', 'bq']:
    for i in range(2):
        for j in range(2):
            st = _struct.Struct(fmt)
