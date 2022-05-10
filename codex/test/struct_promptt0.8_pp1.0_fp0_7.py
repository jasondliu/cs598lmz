import _struct
# Test _struct.Struct()
with self_test():
    for code in 'BHiIlLfdP':
        s = _struct.Struct('!' + code)
        assert s.size == struct.calcsize('!' + code)
