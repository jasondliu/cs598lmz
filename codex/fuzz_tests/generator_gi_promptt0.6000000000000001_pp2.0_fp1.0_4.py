gi = (i for i in ())
# Test gi.gi_code.co_filename
print(str(gi.gi_code.co_filename))
# Test gi.gi_frame.f_code.co_filename
print(str(gi.gi_frame.f_code.co_filename))
# Test gi.gi_frame.f_lineno
print(str(gi.gi_frame.f_lineno))

# Test tp_dict
def test_tp_dict():
    class A:
        pass
    A.a = 10
    print(A.__dict__)

# Test tp_flags
def test_tp_flags():
    class A:
        pass
    print(A.__flags__)

test_tp_dict()
test_tp_flags()

# Test tp_iter
def test_tp_iter():
    class A:
        def __iter__(self):
            return iter(())
    a = A()
    print(next(iter(a)))

test_tp_iter()

# Test tp_richcompare
class A:
    def __eq__
