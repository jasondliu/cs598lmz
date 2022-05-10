import ctypes
# Test ctypes.CField
c_cf = ctypes.CField()
c_cf.size = 4
c_cf.cname = ""
c_cf.type = "int"
c_cf.name = "a"
c_cf.default = 0
def test_20_1():
    """Test ctypes.CField.size"""
    assert c_cf.size == 4
def test_20_2():
    """Test ctypes.CField.cname"""
    assert c_cf.cname == ""
def test_20_3():
    """Test ctypes.CField.type"""
    assert c_cf.type == "int"
def test_20_4():
    """Test ctypes.CField.name"""
    assert c_cf.name == "a"
def test_20_5():
    """Test ctypes.CField.default"""
    assert c_cf.default == 0
def test_20_6():
    """Test ctypes.CField.is_bitfield"""
    assert c_cf.is_bitfield == False
def test_20_7():
