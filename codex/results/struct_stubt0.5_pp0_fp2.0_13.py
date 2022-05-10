from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')

def test_issue_5605():
    # This should not segfault.
    s.pack(0)

def test_issue_5605_b():
    # This should not segfault.
    s.pack(0)
    s.unpack(b'\0\0\0\0')

def test_issue_5605_c():
    # This should not segfault.
    s.pack(0)
    s.unpack(b'\0\0\0\0')
    s.pack(0)

def test_issue_5605_d():
    # This should not segfault.
    s.pack(0)
    s.unpack(b'\0\0\0\0')
    s.pack(0)
    s.unpack(b'\0\0\0\0')

def test_issue_5605_e():
    # This should not segfault.
    s.pack(0)
    s.un
