import codecs
# Test codecs.register_error

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test.xmlcharrefreplace', handler)

class Test_XMLCharRefReplace(unittest.TestCase):
    def test_xmlcharrefreplace(self):
        self.assertEqual(
            u'ab\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd'.encode(
                'ascii', 'test.xmlcharrefreplace'),
            'ab\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd')

if __name__ == "__main__":
    unittest.main()
