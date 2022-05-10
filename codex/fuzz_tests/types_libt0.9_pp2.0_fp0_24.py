import types
types.IntType = int
types.StringType = str
types.UnicodeType = str

import data
import utils

class Test_000_make_an_example_tree(unittest.TestCase):
    def setUp(self):
        data.init()
        data.load('tests/tests.tree')

    def test_000_get_root(self):
        self.assert_(data.ROOT == '/rootdir')

    def test_001_get_dir(self):
        self.assert_(data.DIRS[1].parent.path() == '/rootdir')
        self.assert_(data.DIRS[2].parent.path() == '/rootdir')
        self.assert_(data.DIRS[3].parent.path() == '/rootdir/dir1')
        self.assert_(data.DIRS[4].parent.path() == '/rootdir/dir1')
        self.assert_(data.DIRS[5].parent.path() == '/rootdir/dir2')
        self.assert_(data.DIRS[6].parent.path() == '/
