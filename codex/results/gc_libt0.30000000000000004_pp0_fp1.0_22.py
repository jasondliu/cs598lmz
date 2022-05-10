import gc, weakref

import numpy as np

import pyopencl as cl
import pyopencl.array

import pytest

from boxtree.tools import (
    DeviceDataRecord,
    DeviceDataCollection,
    )


def test_device_data_record():
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    ddr = DeviceDataRecord(ctx, queue, np.float64, (10,))

    assert ddr.dtype == np.float64
    assert ddr.shape == (10,)
    assert ddr.nbytes == 10 * np.float64().nbytes

    assert ddr.cl_mem is None

    ddr.allocate()
    assert ddr.cl_mem is not None

    assert ddr.cl_mem.get_info(cl.mem_info.TYPE) == cl.mem_object_type.BUFFER
    assert ddr.cl_mem.get_info(cl.mem_info.SIZE) == ddr.nbytes

    # --

    ddr.deallocate
