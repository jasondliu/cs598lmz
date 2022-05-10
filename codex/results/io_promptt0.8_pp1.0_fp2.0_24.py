import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'\x01\x02\x03'

with io.open(os.devnull, 'w') as f:
    f.write(MyRawIO().read())

 
###############################################################################
## End of tests
#############################
