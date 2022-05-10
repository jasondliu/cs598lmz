import ctypes
# Test ctypes.CField
test_class = """
class Test:
    x = ctypes.CField()
"""
test_module = source_to_extension(test_class, ['test'])
test_module.test.Test.x.type = ctypes.c_int
id_x = id(test_module.test.Test.x)
test_module.test.Test.y = ctypes.CField()
test_module.test.Test.y.type = ctypes.c_int
id_y = id(test_module.test.Test.y)
test_module.test.Test.x, test_module.test.Test.y
test_obj = test_module.test.Test()
test_obj.x, test_modul
