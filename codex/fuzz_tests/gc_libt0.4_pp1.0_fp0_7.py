import gc, weakref

import numpy as np

import pyopencl as cl
import pyopencl.array
import pyopencl.clrandom
import pyopencl.tools

import pytest

import loopy as lp
import loopy as lp
from loopy.diagnostic import LoopyError
from loopy.kernel.data import (
        AddressSpace, ArrayBase, ConstantArg,
        GlobalArg, ValueArg, TemporaryVariable,
        ImageArg,
        )
from loopy.kernel.array import (
        ArrayBase,
        ConstantArg,
        GlobalArg,
        ValueArg,
        TemporaryVariable,
        ImageArg,
        )
from loopy.kernel.tools import (
        DomainChanger,
        )
from loopy.types import to_loopy_type

import logging
logger = logging.getLogger(__name__)


def test_array_arg_instantiation():
    knl = lp.make_kernel(
            "{[i,j]: 0<=i,j<10}",
            """
            a[i] = 2
