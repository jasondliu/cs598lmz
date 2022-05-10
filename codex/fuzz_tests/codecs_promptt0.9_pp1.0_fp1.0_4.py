import codecs
# Test codecs.register_error.
# http://bugs.python.org/issue1376231
codecs.register_error("test.replace", codecs.replace_errors)
with self.assertRaises(KeyError):
    codecs.register_error("test.replace", codecs.replace_errors)

t1, t2 = ("ignore",), ("xmlcharrefreplace",)
codecs.register_error("test.ignore", codecs.ignore_errors)
codecs.register_error("test.xmlcharrefreplace", codecs.xmlcharrefreplace_errors)
self.assertEquals(tuple(codecs.lookup_error("test.ignore"))[:2], t1)
self.assertEquals(tuple(codecs.lookup_error("test.xmlcharrefreplace"))[:2], t2)

# http://bugs.python.org/issue1376214
x = "äöü".encode("iso-8859-1")
self.assertTrue(x.decode("latin1", errors="strict") ==
                x.decode("
