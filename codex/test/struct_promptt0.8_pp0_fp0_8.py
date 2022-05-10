import _struct
# Test _struct.StructType().__new__
module = _struct
def test_new():
    struct_type = module.StructType
    # 1.
    class TestStruct(struct_type('TestStruct', 'a b')):
        pass

    # 2.
    TestStruct = struct_type('TestStruct', 'a b', target='TestStruct')

    # 3.
    class TestStruct(struct_type('TestStruct', 'a b')):
        @classmethod
        def __prepare__(metacls, name, bases):
            return {}

    # 4.
    class TestStruct(struct_type('TestStruct', 'a b')):
        @classmethod
        def __prepare__(metacls, name, bases):
            return {'__module__': 'test'}

    # 5.
    class TestStruct(struct_type('TestStruct', 'a b')):
        __dict__ = {'__module__': 'test'}

    # 6.
    @struct_type('TestStruct', 'a b')
    class TestStruct:
        pass

    # 7.

