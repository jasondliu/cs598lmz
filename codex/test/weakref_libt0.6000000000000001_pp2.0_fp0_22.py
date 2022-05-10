import weakref

import numpy as np

from chainer.backends import cuda
from chainer.dataset import convert
from chainer.dataset import iterator as iterator_module
from chainer import function
from chainer import function_hook
from chainer import link
from chainer import reporter as reporter_module
from chainer import variable


class _EvaluatorHook(function_hook.FunctionHook):

    name = 'EvaluatorHook'

    def __init__(self):
        self.dataset = None
        self.iterator = None

    def __call__(self, func, in_data):
        in_vars, out_vars = func.inputs, func.outputs
        self.evaluator.evaluate(in_vars, out_vars)

    def finalize(self):
        self.evaluator.finalize()


