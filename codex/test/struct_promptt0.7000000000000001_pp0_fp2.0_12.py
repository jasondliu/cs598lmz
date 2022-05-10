import _struct
# Test _struct.Struct with alignment
#
# In order to test alignment, we need to be able to use memory which has
# a different alignment than the struct module.

alignment = _struct.calcsize('P')

# This class is a buffer with a different alignment
class AlignedBuffer:
    def __init__(self, contents):
        # Allocate some memory
        self.allocated_buffer = ctypes.create_string_buffer(contents)
        # Now, allocate some more memory, which we'll discard
        self.discard_buffer = ctypes.create_string_buffer(contents)
        # Now, get the address of the two buffers
        self.allocated_address = ctypes.addressof(self.allocated_buffer)
        self.discard_address = ctypes.addressof(self.discard_buffer)
        # And get the difference between them, so we can adjust the
        # address.
        self.adjustment = self.allocated_address - self.discard_address

