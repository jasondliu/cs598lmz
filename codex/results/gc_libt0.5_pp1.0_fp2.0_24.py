import gc, weakref
import numpy as np
from numpy.testing import assert_equal
from pyoperators import (
    BlockColumnOperator, BlockRowOperator, BlockDiagonalOperator,
    BlockDiagonalOperatorLinear, BlockRowOperatorLinear,
    BlockColumnOperatorLinear, BlockDiagonalOperatorNonLinear,
    BlockRowOperatorNonLinear, BlockColumnOperatorNonLinear,
    BlockDiagonalOperatorDerivative, BlockRowOperatorDerivative,
    BlockColumnOperatorDerivative, BlockDiagonalOperatorInverse,
    BlockRowOperatorInverse, BlockColumnOperatorInverse,
    BlockDiagonalOperatorComposition, BlockRowOperatorComposition,
    BlockColumnOperatorComposition, BlockDiagonalOperatorTranspose,
    BlockRowOperatorTranspose, BlockColumnOperatorTranspose,
    BlockDiagonalOperatorAdjoint, BlockRowOperatorAdjoint,
    BlockColumnOperatorAdjoint, BlockDiagonalOperatorConjugate,
    BlockRowOperatorConjugate, BlockColumnOperatorConjugate,
   
