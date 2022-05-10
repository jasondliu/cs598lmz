import _struct
# Test _struct.Struct.unpack_from
struct_pack = _struct.Struct('i').pack
class TestUnpackFrom :
    def _test(self, extra_args, test_args, format_str, value):
        # test_args are the args for the test function:
        #     unpack_from(format, buffer[, offset])
        # extra_args are the args to unpack() (must be a tuple):
        #     unpack(format, buffer[, offset])
        # If extra_args is None, then we don't call unpack().
        buf = struct_pack(format_str, value)
        fmt = _struct.Struct(format_str)
        offset = test_args[2]
        # Check test_args and extra_args don't have an offset,
        # (or if they do, ensure it's the same offset).
        assert len(test_args) <= 3
        if extra_args is not None:
            assert len(extra_args) <= 3
            if len(extra_args) == 3:
                assert extra_args[2] == offset
        #
