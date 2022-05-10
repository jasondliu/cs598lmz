import weakref

from numpy.testing import assert_array_equal, assert_array_almost_equal

from pytest import raises

from arlpy.testing import close_all_plots
from arlpy.plotting import *


class TestPlotting:
    def test_removeall(self):
        lines, = plt.plot([1, 2, 3])
        assert len(plt.gca().lines) == 1
        remove_all_lines()
        assert len(plt.gca().lines) == 0
        close_all_plots()

    def test_remove_all_lines(self):
        lines1, = plt.plot([1, 2, 3])
        lines2, = plt.plot([4, 5, 6])
        remove_all_lines_from_axes([plt.gca()])
        assert len(plt.gca().lines) == 0
        close_all_plots()

    def test_remove_all_artists(self):
        plt.plot([1, 2, 3])
        plt
