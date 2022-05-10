import codecs
# Test codecs.register_error
def ucs_replace(exception):
    return ('*** ', exception.end)
codecs.register_error('test.ucs_replace', ucs_replace)
class TranslationTestBase:
    encoding = None
    tstring = None
    def check_exception(self, obj, methodname, *args):
        method = getattr(obj, methodname)
        try:
            method(*args)
        except self.exception as value:
            if str(value) == self.errorstr:
                pass
            else:
                self.fail("wrong exception (%s != %s)" % (str(value),
                                                          self.errorstr))
        else:
            self.fail("didn't get expected exception")
    def check_result(self, obj, methodname, *args):
        method = getattr(obj, methodname)
        s = method(*args)
        self.assertEqual(s, self.translation)
class String_TranslationTestBase:
    encoding = None
    tstring = None
    tstrings = None
