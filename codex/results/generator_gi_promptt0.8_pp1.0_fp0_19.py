gi = (i for i in ())
# Test gi.gi_code is None
#
# test_iter: UnboundLocalError("local variable 'i' referenced before assignment")
# test_iter: UnboundLocalError("local variable 'i' referenced before assignment")
# test_iter: AttributeError("'generator' object has no attribute 'gi_code'")
# test_iter: AttributeError("'generator' object has no attribute 'gi_code'")

# test_iter: UnboundLocalError("local variable 'i' referenced before assignment")
# test_iter: UnboundLocalError("local variable 'i' referenced before assignment")
# test_iter: system error: Bad address
# test_iter: system error: Bad address
