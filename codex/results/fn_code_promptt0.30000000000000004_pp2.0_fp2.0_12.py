fn = lambda: None
# Test fn.__code__.co_filename
class Test(unittest.TestCase):
    def test_filename(self):
        self.assertEqual(fn.__code__.co_filename, '<string>')


if __name__ == "__main__":
    unittest.main()
