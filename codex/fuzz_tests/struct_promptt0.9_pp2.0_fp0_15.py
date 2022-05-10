import _struct
# Test _struct.Struct
s = _struct.Struct("c1")
a = s.pack("a")
b = s.pack("b")
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(a)
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(b)
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(a)
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(b)
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(a)
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(b)
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(a)
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(b)
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(a)
%micro benchmark -m timeit -r 1 -n 10000 s.unpack(b)
%micro benchmark -m timeit -r 1 -n 10000 s.un
