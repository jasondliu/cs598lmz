import types
# Test types.FunctionType
import unittest
import urllib


def _Escape(text):
  return urllib.quote(text, safe='/=')


class TestMapWithBuildConstant(basetest.TestCase):
  def setUp(self):
    self.mox.StubOutWithMock(write.FileBacked, 'Get')
    self.path1 = '/home/username/myapp/app.yaml'
    self.path2 = '/home/username/myapp/app2.yaml'
    self.application = 'app2'
    self.version = 'version2'
    self.base_url = 'http://www.example.com/bar'

  def testBasic(self):
    """Only the filenames change in the rewrite_rule section."""
    router_contents1 = """rewrite_rule:
- match: ^foo match: ^bar
  spider: false
  action: redirect:
    url: http://www.example.com/bar/foo
    type: redirect
  login: admin
- match: ^foo1
