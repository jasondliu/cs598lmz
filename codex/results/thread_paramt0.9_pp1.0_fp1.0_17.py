import sys, threading
threading.Thread(target=lambda: sys.stdout.write('python\n')).start()

with open('a.out', 'rb') as f:
    code = f.read()

assert theano.sandbox.cuda.cuda_enabled == False
mycode = theano.sandbox.cuda.compile_cuda_kernel(code, 'tensorContractionKernel', 0)
assert not isinstance(mycode, str)

f = theano.function([T.TensorType.make_tensor_type()('x', T.TensorType.make_vector()(False), broadcastable=(False, True))],
                    T.TensorType.make_tensor_type()('x', T.TensorType.make_vector()(False), broadcastable=(False, True))(T.TensorType.make_tensor_type()('temp', T.TensorType.make_vector()(False), broadcastable=(False, False))(mycode)),
                    mode='Eval')

print f(numpy.array([[1, 2], [3, 4]], dtype=
