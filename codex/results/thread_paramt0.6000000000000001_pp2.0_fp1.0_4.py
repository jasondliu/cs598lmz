import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

#
#	Use the TensorFlow for Poets image classifier
#
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
sess = tf.InteractiveSession()

#
#	Define the softmax regression model
#
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
sess.run(tf.global_variables_initializer())
y = tf.matmul(x, W) + b

#
#	Define the loss and optimizer
#
cross_entropy = tf.reduce_
