import select
# Test select.select and select.poll implementations
import unittest
from test.support import (skip_unless_symlink, TESTFN, run_with_locale,
                          reap_children, unlink)
import time
timeout = 60


@skip_unless_symlink
class SelectSelectTestCase(unittest.TestCase):

    def test_select(self):
        cmd = 'for i in 0 1 2 3 4 5 6 7 8 9; do echo testing...; sleep 1; done'
        p = subprocess.Popen(cmd, shell=1,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
