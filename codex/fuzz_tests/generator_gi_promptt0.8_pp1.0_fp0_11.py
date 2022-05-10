gi = (i for i in ())
# Test gi.gi_code
print(next(gi))
# 2.2.2.2
# test.test_contains(): Exception: no!
# 2.2.2.3
# test.test_isinstance(): Exception: no!
# 2.2.2.4
# Test with_cmp() function
import test.test_comparisons
test.test_comparisons.with_cmp()
# Test mycmp() function
import test.test_comparisons
test.test_comparisons.mycmp()
# Test bool() function
import test.test_comparisons
test.test_comparisons.C1()
# 2.2.3.1
# Test member.__init__() function
class member:
    def __init__(self, type, name, offset):
        self.type, self.name, self.offset = type, name, offset
# Test member.__init__() function
mem_dict = {'a': member('int', 'a', 0),
            'b': member('double', 'b', 4)}
print(mem_dict['a'].offset
