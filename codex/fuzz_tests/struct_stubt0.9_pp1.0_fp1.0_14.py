from _struct import Struct
s = Struct.__new__(Struct)
print(type(s))

# Try to do something structured.

s.format = '<IQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQIQ'
s.size = s.calcsize(s.format)
print(repr(s.format))
print(repr(s.size))

# So we have a 74-byte header.  Let's read past that header to the first page of call stack data.

fp.seek(s.size)
traces = s.unpack(fp.read(s.size))
print(len(traces), type(traces))
print(traces)


# Let's choose a particular datum to be our loop invariant (accumulator of the stack traces)
# and see how we can visualize it using R.

invariants = traces[1:6] + traces[8:67:2]
print(invariants)



# THIS IS BROKEN.  I'M NOT SURE IF IT'S B
