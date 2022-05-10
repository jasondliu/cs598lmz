import types
types.ModuleType.__repr__ = lambda self: self.__name__

class Test(unittest.TestCase):
    def test_read_data(self):
        data = read_data('day-01.txt')
        self.assertEqual(type(data), str)

    def test_parse_data(self):
        data = read_data('day-01.txt')
        self.assertEqual(type(parse_data(data)), list)

    def test_calc_fuel(self):
        self.assertEqual(calc_fuel(12), 2)
        self.assertEqual(calc_fuel(14), 2)
        self.assertEqual(calc_fuel(1969), 654)
        self.assertEqual(calc_fuel(100756), 33583)

    def test_calc_fuel_recursive(self):
        self.assertEqual(calc_fuel_recursive(14), 2)
        self.assertEqual(calc_fuel_recursive(1969), 966)
        self.assertE
