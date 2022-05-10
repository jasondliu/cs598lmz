gi = (i for i in ())
# Test gi.gi_code exists, it will be removed on Python 3.
gi.gi_code

# Test if gi returns gi.gi_frame as its tb_frame
assert next(gi) is gi.gi_frame


def f1():
    return iter(lambda: 0, None)


def f2():
    return iter(lambda: 0, None)


def f3():
    return iter(lambda: 0, None)


_, _, traceback1 = sys.exc_info()
traceback2 = f1().gi_frame.f_back
traceback3 = f2().gi_frame.f_back
traceback4 = f3().gi_frame.f_back

# Test tb_next
assert traceback1.tb_next is traceback2
assert traceback2.tb_next is traceback1

# Test tb_next
assert traceback2.tb_next is traceback1
assert traceback1.tb_next is traceback2

# Test tb_frame
assert traceback1.tb_frame is f1.
