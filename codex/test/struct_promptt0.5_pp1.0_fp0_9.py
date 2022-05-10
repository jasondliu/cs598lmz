import _struct
# Test _struct.Struct.
def test_struct():
    def check(st, fmt, sz, alignment):
        assert st.format == fmt
        assert st.size == sz
        assert st.alignment == alignment

    check(Struct('x'), 'x', 1, 1)
    check(Struct('xi'), 'xi', 5, 4)
    check(Struct('xh'), 'xh', 3, 2)
    check(Struct('xl'), 'xl', 9, 4)
    check(Struct('xq'), 'xq', 17, 8)
    check(Struct('c'), 'c', 1, 1)
    check(Struct('b'), 'b', 1, 1)
    check(Struct('B'), 'B', 1, 1)
    check(Struct('h'), 'h', 2, 2)
    check(Struct('H'), 'H', 2, 2)
    check(Struct('i'), 'i', 4, 4)
    check(Struct('I'), 'I', 4, 4)
    check(Struct('l'), 'l', 4, 4)
