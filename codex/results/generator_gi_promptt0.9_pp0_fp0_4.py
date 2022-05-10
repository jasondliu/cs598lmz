gi = (i for i in ())
# Test gi.gi_code.co_flags
# gi.gi_code.co_flags &= 0xFF
# Test gi.gi_code.co_name

# Verify generators
def behave_like_generator():
    try:
        gen = (i for i in ())
        gen.gi_code.co_flags &= 0xFF
        assert contains_non_yield_code(gen)
        return True
    except:
        return False

def behave_like_generator_gen():
    try:
        gen = (i for i in ())
        gen.gi_code.co_flags &= 0xFF
        assert contains_non_yield_code(gen)
        assert gen.gi_code.co_name == '<genexpr>'
        return True
    except:
        return False

def behave_like_generator_func():
    def _x(x):
        return 1
    try:
        gen = ((1,), i for i in ())
        gen.gi_code.co_flags &= 0xFF
        assert contains_non_
