fn = lambda: None
# Test fn.__code__.co_filename, which is a real attr, but in Python 2 returns a
# string.
class TestAttrCodeFilename(object):
  def test_attr_code_filename(self):
    fn.__code__.co_filename = 'test_attr_code_filename'
    self.assertListEqual(
      [repr(fn.__code__.co_filename)],
      [] if sys.version_info.major == 3 else ['"test_attr_code_filename"']
    )

TestAttrCodeFilename().test_attr_code_filename()
