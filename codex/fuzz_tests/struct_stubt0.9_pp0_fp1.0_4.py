from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 32
s.pack = lambda *x: b''
s.unpack = lambda x: tuple([0] * len(x))


class ConversionsTests(unittest.TestCase):
    def test_tableName(self):
        self.assertEqual(tableName('details'), 'details')
        self.assertEqual(tableName('details_with_dashes'), 'details_with_dashes')
        self.assertEqual(tableName('details with spaces and numbers 8437'), 'details_with_spaces_and_numbers_8437')
        self.assertEqual(tableName('headers and spaces'), 'headers_and_spaces')
        self.assertEqual(tableName('it \t has \t faired \t well '), 'it_has_faired_well')
        self.assertEqual(tableName(' § # % &'), '$___&')
        self.assertEqual(tableName(' $ # % & % ## %'), '$_____&____')

    def test_columnName(self):
        self
