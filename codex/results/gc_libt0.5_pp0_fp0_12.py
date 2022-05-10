import gc, weakref

import numpy as np

import pyopencl as cl
import pyopencl.array
import pyopencl.clrandom
import pyopencl.elementwise

import pytest

def test_mem_host_to_device_with_pending_operation():
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    a = cl.array.empty(queue, (12,), dtype=np.dtype("i4"))
    b = a.copy()

    a.fill(1, queue=queue)

    with pytest.raises(RuntimeError):
        cl.enqueue_copy(queue, a.data, b.data)

def test_mem_host_to_device_with_pending_operation_via_map():
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    a = cl.array.empty(queue, (12,), dtype=np.dtype("i4"))
    b = a.copy()

    a.fill(1
