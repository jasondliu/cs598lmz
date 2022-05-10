import gc, weakref
from threading import Thread

from onnx import helper, TensorProto
from onnx import numpy_helper


class Worker(Thread):
    def __init__(self, in_queue, out_queue):
        Thread.__init__(self)
        self.daemon = True
        self._in_queue = in_queue
        self._out_queue = out_queue
        self._run = True

    def run(self):
        while self._run:
            msg = self._in_queue.get()
            if msg is None:
                self._run = False
                self._in_queue.task_done()
            else:
                name, tensor, name_to_tensor = msg
                tensor = helper.make_tensor(
                    name, tensor.dtype, tensor.shape, tensor.data)
                name_to_tensor[name] = tensor
                self._out_queue.put(tensor)
                self._in_queue.task_done()


class DummyThread(Thread):
    def
