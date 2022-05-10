fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# This is a bit of a hack, but it lets us
# raise the recursion limit as high as we need
# to, to make sure that our tests don't fail
# because of the default limit of 1000 frames
sys.setrecursionlimit(1000000)

# This is the list of test cases.  Each test case is a tuple
# that contains five values:
#   - the string to parse (may be None if the test case is
#     expected to fail during scanning)
#   - the string that should be produced by the pretty-printer
#     (may be None if the test case is expected to fail during
#      pretty-printing)
#   - the string that should be produced by the code generator
#     (may be None if the test case is expected to fail during
#      code generation)
#   - the expected value of the test case (may be None if the
#     test case is expected to fail during execution)
#   - the expected type of the test case (may be None if the
#     test case is expected to fail during execution)
test_cases = [

