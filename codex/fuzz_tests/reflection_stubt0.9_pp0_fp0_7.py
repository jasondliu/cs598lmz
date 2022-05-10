fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi, fn
class A(dict):
  def __default_get(self, key, default):
    return default
A.__getitem__ = A.__missing__ = A.__default_get
a = A()
a[10]
''')
    self.assertEquals('', out)
    self.assertEquals('', err)

  @with_env(PYTHON_PATH=None)
  def test_bad_path(self):
    out, err, rc = self._run('''
import os
os.chdir('/')
import sys
sys.path.append('/this_directory_does_not_exist')
from subprocess import *
Popen(["python", "-c", "print('abc')"]).communicate()
''')
    self.assertEquals('', out)
    self.assertEquals('', err)

  @with_env(PYTHON_PATH=None)
  def test_bad_package_init(self):
    out, err, rc = self._run('''

