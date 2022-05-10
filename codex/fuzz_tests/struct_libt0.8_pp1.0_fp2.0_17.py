import _struct
import io


class TestStruct(unittest.TestCase):
    """
    Tests for the _struct module.
    """
    def test_pack_unpack(self):
        # Test pack and unpack.
        bins = [
            b('12345'),
            b('12345678901234567890'),
        ]
        for siz in range(1, 32):
            bins.append(b('\000' * siz))
        # Test a variety of different formats against each string
        for bin in bins:
            for code in all_codes:
                format = '=' + code
                size = struct.calcsize(format)
                args = range(struct.calcsize(format))
                res = struct.pack(format, *args)
                # print `res`, `bin[:size]`
                self.assertEqual(res, bin[:size])
                if verbose:
                    print("    testing: struct.pack/unpack('%s')" % format)
                x = struct.unpack(format, bin[:size])
