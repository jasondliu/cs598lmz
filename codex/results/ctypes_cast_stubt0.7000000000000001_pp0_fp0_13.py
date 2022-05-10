import ctypes
ctypes.cast(0, ctypes.py_object)

X = tf.placeholder("float", [None, 784]) # create symbolic variables
W1 = tf.Variable(np.float32(np.random.rand(784, 10))*0.1)
b1 = tf.Variable(np.float32(np.random.rand(10))*0.1)

W2 = tf.Variable(np.float32(np.random.rand(10, 10))*0.1)
b2 = tf.Variable(np.float32(np.random.rand(10))*0.1)

W3 = tf.Variable(np.float32(np.random.rand(10, 10))*0.1)
b3 = tf.Variable(np.float32(np.random.rand(10))*0.1)

W4 = tf.Variable(np.float32(np.random.rand(10, 10))*0.1)
b4 = tf.Variable(np.float32(np.random.rand(10))*0.1)

W5 = tf
