import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(object):
    def __init__(self):
        self.x = 1

def test_struct_member_access():
    s = S()
    s.x = 1
    assert s.x == 1
    assert type(s.x) is int

def test_struct_member_access_with_instance():
    s = S()
    s.x = C()
    assert s.x.x == 1
    assert type(s.x) is C

def test_struct_member_access_with_instance_and_int():
    s = S()
    s.x = C()
    s.x.x = 2
    assert s.x.x == 2
    assert type(s.x) is C

def test_struct_member_access_with_instance_and_int_and_instance():
    s = S()
    s.x = C()
    s.x.x = 2
    s.x = C()
    assert s.x.x == 1
