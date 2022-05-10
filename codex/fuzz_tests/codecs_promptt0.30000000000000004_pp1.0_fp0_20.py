import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

class Test_SearchFunction(unittest.TestCase):
    def test_search_function(self):
        self.assertEqual('abc'.encode('test.searchfunction'), b'abc')
        self.assertEqual(b'abc'.decode('test.searchfunction'), 'abc')

def test_main():
    test_support.run_unittest(Test_SearchFunction)

if __name__ == "__main__":
    test_main()
