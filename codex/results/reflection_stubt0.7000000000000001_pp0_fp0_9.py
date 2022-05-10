fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code  # type: ignore

# https://github.com/python/cpython/blob/v3.7.2/Lib/test/pickletester.py#L1230-L1253
def _assert_equal(self, proto, unpickled, original):
    self.assertIs(type(original), type(unpickled))
    try:
        self.assertEqual(original, unpickled)
    except Exception:
        # For some types, we need to look at the pickled
        # form to see the difference.
        pickled = self._pickle(unpickled, proto)
        self.fail(f"{repr(original)} != {repr(unpickled)} (proto={proto})\n"
                  f"  pickle of 'unpickled': {repr(pickled)}")

# https://github.com/python/cpython/blob/v3.7.2/Lib/test/pickletester.py#L1255-L1261
def _assert_not_equal(self,
