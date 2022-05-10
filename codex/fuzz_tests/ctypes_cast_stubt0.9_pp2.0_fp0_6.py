import ctypes
ctypes.cast(image, ctypes.c_void_p)


# Define the data type and shape, then create placeholders for the variables.
X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, 7])
 
# Initialize the weights and biases.
W = tf.Variable(tf.zeros([784, 7]))
b = tf.Variable(tf.zeros([7]))
 
# The machine learning model.
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)
 
run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
run_metadata = tf.RunMetadata()

# Set up the loss, optimizer, and accuracy.
loss = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), reduction_indices=[1]))
optimizer =  tf.train.GradientDescentOptimizer(0.1).minimize(
