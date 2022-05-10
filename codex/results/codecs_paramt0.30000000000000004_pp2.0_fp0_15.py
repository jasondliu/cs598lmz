import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_sorted_by_key(unittest.TestCase):
    def test_sorted_by_key(self):
        self.assertEqual(sorted_by_key([{'a': 1}, {'a': 2}, {'a': 3}], 'a'), [{'a': 1}, {'a': 2}, {'a': 3}])
        self.assertEqual(sorted_by_key([{'a': 3}, {'a': 2}, {'a': 1}], 'a'), [{'a': 1}, {'a': 2}, {'a': 3}])
        self.assertEqual(sorted_by_key([{'a': 3}, {'a': 2}, {'a': 1}], 'b'), [{'a': 3}, {'a': 2}, {'a': 1}])
        self.assertEqual(sorted_by_key([{'a': 3}, {'a': 2}, {'a': 1}], 'a', reverse=True),
