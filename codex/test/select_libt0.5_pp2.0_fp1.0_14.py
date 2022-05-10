import selectors
import sys
import types

# TODO: Implement tests for the following methods:
# * run_once
# * close
# * fileno
# * select
# * register
# * unregister
# * modify
# * get_key
# * get_map
# * from
# * install
# * open
# * get_current_map
# * set_blocked
# * set_wakeup_fd
# * devpoll
# * epoll
# * fromfd
# * kqueue
# * poll
# * select


class TestSelectors(unittest.TestCase):

    def test_BaseSelector(self):
        b = selectors.BaseSelector()
        with self.assertRaises(NotImplementedError):
            b.select(timeout=None)
        with self.assertRaises(NotImplementedError):
            b.register(0, selectors.EVENT_READ)
        with self.assertRaises(NotImplementedError):
            b.unregister(0)
