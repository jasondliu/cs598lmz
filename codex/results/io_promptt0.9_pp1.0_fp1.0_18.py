import io
# Test io.RawIOBase handling

with io.BytesIO(b"foo") as fobj:
    o = io.RawIOBase()
    o.readinto(fobj)
 
with io.BytesIO(b"foo") as fobj:
    o = io.RawIOBase()
    o.readinto1(fobj)

# Test ssz.DecodeError

o = ssz.DecodeError(1, "Test")
o = ssz.DecodeError(1, "Test", 'abc')
 
# Test ssz.InvalidBlockError

o = ssz.InvalidBlockError("Test")
    
# Test ssz.NoTreehashFn

o = ssz.NoTreehashFn()

# Test ssz.TooBigObjectError

o = ssz.TooBigObjectError(1)

# Test ssz.ValidationError

o = ssz.ValidationError("Test")
    
# Test ssz.TreehashError

o = ssz.TreehashError(1)

# Test ssz.SerializationError

o =
