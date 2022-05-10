import gc, weakref
import pytest
import weakref

from bluesky.utils import ProgressBarManager as pbm

@pytest.fixture(scope='function')
def pb():
    return pbm()


class TestProgressBarManager:
    def test_a_new_default_manager_has_no_bars(self, pb):
        assert len(pb._bars) == 0

    def test_an_existing_manager_does_not_have_new_bars(self, pb):
        first = pbm.register('first')
        assert len(pb._bars) == 1

        second = pbm.register('second')
        assert len(pb._bars) == 2

        assert len(first._bars) == 1
        assert len(second._bars) == 1
        assert len(pb._bars) == 0

        first.close()
        second.close()

    def test_register_returns_the_same_progress_bar(self, pb):
        # Register once.
        bar1 = pbm.register('test1')

        assert len(pb._bars)
