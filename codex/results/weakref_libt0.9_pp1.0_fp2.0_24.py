import weakref

import crypto.tools.mathscript as mathscript

from crypto.analysis.metrics.generic import *

class Permutation(object):
    """Permutation abstract base class

    Keyword arguments:
    block_size -- the size of a block (or permutation application) in bits
    """
    def __init__(self, block_size):
        self.block_size = block_size

    def __call__(self, x):
        """Calls the permutation, which is assumed to be a bijection.

        Required arguments:
        x -- the input bitstring

        Returns:
        The permutated bitstring.
        """
        return NotImplementedError()

    def inverse(self, y):
        """Finds the inverse of the permutation. The optional inverse
        argument indicates whether or not to create a new Permutation object
        or return a function as the inverse.

        Required arguments:
        y -- the output of the permutation

        Keyword arguments:
        NewPermutation -- a class argument for the new permutation. This is
               necessary to avoid
