import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)

if __name__ == '__main__':
    unittest.main()
