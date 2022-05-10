import codecs
codecs.register_error('xmlcharrefreplace', xmlcharrefreplace_errors())

from cfg import *
from downloader import *
import cProfile, pstats

class TestDownloader(unittest.TestCase):
  
  def setUp(self):
    self.pr = cProfile.Profile()
    self.pr.enable()
    self.downloader = Downloader()
    self.downloader.reset()
  
  def tearDown(self):
    self.pr.disable()
    ps = pstats.Stats(self.pr)
    ps.sort_stats('cumulative')
    ps.print_stats(0.01)
  
  def _do_action(self, action):
    change_set = self.downloader.process_action(action)
    self.downloader.process_changeset(change_set)
    self.assertTrue(len(change_set) > 0)
  
  def test_follow(self):
    self._do_action({'user':'user1', 'action':'follow', 'target':'user2', 'type':'user
