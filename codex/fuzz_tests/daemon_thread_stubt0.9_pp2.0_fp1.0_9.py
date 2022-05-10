import sys, threading

def run():
    n = 1000000
    engine = xrt.Engine(xrt.Backend.u50.CUDA)

    h_buf = buffer_from_ndarray(np.random.rand(n).astype(np.float32))

    shape = xrt.boolean_shape((n,))
    buf = engine.allocate(shape)
    stream = engine.stream()

    ops = np.greater(h_buf.to_pybytes(), 0.5).astype(np.int32)
    engine.upload(h_buf, stream=stream)
    engine.download(ops, buf, stream=stream)
    stream.synchronize()

    assert False not in ops, ops

runs = []

for i in range(2):
    t = threading.Thread(target=run)
    t.start()
    runs.append(t)

while runs:
    runs.pop().join()
