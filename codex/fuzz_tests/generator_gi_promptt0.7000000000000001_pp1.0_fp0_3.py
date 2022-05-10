gi = (i for i in ())
# Test gi.gi_code.co_flags for for generator flags.
# Bit 0 == CO_GENERATOR_ALLOWED
# Bit 1 == CO_FUTURE_DIVISION
# Bit 2 == CO_FUTURE_ABSOLUTE_IMPORT
# Bit 3 == CO_FUTURE_WITH_STATEMENT
# Bit 4 == CO_FUTURE_PRINT_FUNCTION
# Bit 5 == CO_FUTURE_UNICODE_LITERALS
gi.gi_code.co_flags |= 0x20
# Set gi.gi_frame to an empty frame
gi.gi_frame = types.FrameType(gi.gi_frame.f_globals, gi.gi_frame.f_locals,
                              gi.gi_frame.f_code, gi.gi_frame.f_back)

def next(self):
    """
    Get the next item from the iterator. If a .next() method is defined,
    call that to get the next value. Otherwise, raise StopIteration.
    """
    if self.gi_running:
       
