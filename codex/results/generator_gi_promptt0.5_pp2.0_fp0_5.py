gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags)
# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)
# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)
# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)


class A:
    def __getitem__(self, index):
        return index


a = A()
# Test getitem with a class
print(a[1])

# Test getitem with a list
print([
