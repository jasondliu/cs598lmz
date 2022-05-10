import weakref

import numpy
import six

from chainer import cuda
from chainer import function
from chainer import utils
from chainer.utils import type_check


class BatchNormalization(function.Function):

    """Batch normalization function."""

    def __init__(self, eps=2e-5, mean=None, var=None):
        self.eps = eps
        self.avg_mean = mean
        self.avg_var = var

    def check_type_forward(self, in_types):
        type_check.expect(in_types.size() == 3)

        x_type, gamma_type, beta_type = in_types
        type_check.expect(
            x_type.dtype.kind == 'f',
            gamma_type.dtype == x_type.dtype,
            beta_type.dtype == x_type.dtype,
            gamma_type.shape == beta_type.shape,
            gamma_type.shape == (x_type.shape[1],))

    def forward
