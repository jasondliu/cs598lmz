import weakref

import numpy as np

from nipy.modalities.fmri.glm import make_dmtx

from nose.tools import assert_true, assert_false
from numpy.testing import assert_equal, assert_array_equal

from .test_glm import generate_data


class test_make_dmtx(object):

    def setup(self):
        np.random.seed(0)
        self.Y, self.X = generate_data('basic')
        self.conds = [ 'rest', 'left', 'right']
        self.durations = [45., 30., 30.]
        self.dmtx = make_dmtx(self.conds, self.durations, self.X)

    def test_top_rows_correct(self):
        expected = np.hstack([np.eye(3) * 45., np.eye(3) * 30.,
                              np.eye(3) * 30.])
        expected /= 100.
        ntpts = expected.shape[1]
        assert_array_equal
