gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame.
self.assertEqual(gi.gi_code.co_name, "mygen")
self.assertIs(gi.gi_frame.f_code.co_name, "mygen")
# catch StopIteration
gi.gi_frame = None
gi.gi_code = None
#
gi = (i for i in (),)
# Test gi.gi_code and gi.gi_frame.
self.assertEqual(gi.gi_code.co_name, "comprehension")
self.assertIs(gi.gi_frame.f_code.co_name, "comprehension")
# catch StopIteration
gi.gi_frame = None
gi.gi_code = None
#
# In Py3.5, inspect can handle async def functions.
#
# Example from PEP 492:

async def fact(n):
    f = 1
    while n > 1:
        f = await step(f, n)
        n -= 1
    return f

# (xxx This example needs updating for cor
