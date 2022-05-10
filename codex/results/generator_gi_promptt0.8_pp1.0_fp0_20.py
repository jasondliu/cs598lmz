gi = (i for i in ())
# Test gi.gi_code is NULL


class C(object):
    """ Test that we can inspect a class object """
    def m(self):
        pass

print("before")
print(inspect.getmembers(C))
print("after")

# Test function annotation inspection
def f1(a: 'annotation') -> "Nothing":
    return a

annotations = inspect.getfullargspec(f1).annotations
assert annotations == {'a': 'annotation', 'return': 'Nothing'}

# Test exceptions are inspected properly
import sys
res = inspect.getmembers(sys.float_info)
res.sort()
exp = ("comp_dig", "denorm_min", "dig", "epsilon", "inf", "max", "max_10_exp",
       "max_exp", "min", "min_10_exp", "min_exp", "mant_dig", "nan", "neginf",
       "resolution", "tiny")
for i, r in enumerate(res):
    if r[0] != exp[i]:
        raise AssertionError("
