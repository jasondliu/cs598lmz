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

