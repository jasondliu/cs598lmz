import _struct
# Test _struct.Struct 
# The format string for the struct module is different from the one used for the struct module
# To read "S" you need to use "s"
# To read "I" you need to use "i"
# To read "L" you need to use "l"
# To read "B" you need to use "b"
# To read "H" you need to use "h"
struct_str_1 = "s"
struct_str_2 = "i"
struct_str_3 = "l"
struct_str_4 = "b"
struct_str_5 = "h"
struct_str = struct_str_1 + struct_str_2 + struct_str_3 + struct_str_4 + struct_str_5
struct_obj = _struct.Struct(struct_str)
# print struct_obj.size

class StructTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def test_struct_read_01(self):
        s = "Hello"
        int
