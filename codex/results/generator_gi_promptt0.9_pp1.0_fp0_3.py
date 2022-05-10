gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
print(gi.gi_frame)
print(gi.gi_running)

# Test gi.gi_code == types.GetSetDescriptorType.im_func.func_code
"""
    <py>
    gi = generator(i for i in ())
    self.assertEqual(
        gi.gi_code,
        types.GetSetDescriptorType.im_func.func_code)
    """)

# Cleanup from other tests
del class_
del instance_
del generator
del gi
