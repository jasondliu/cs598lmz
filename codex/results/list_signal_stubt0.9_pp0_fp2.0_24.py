import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def tensor_cpu():
    with tf.device('/cpu:0'):
        # Create a large sparse tensor
        bm = tf.sparse_placeholder(tf.float32)
        rl = tf.sparse_reduce_sum(bm, 1)
    config = tf.ConfigProto(log_device_placement=False)
    config.operation_timeout_in_ms = 5000
    with tf.Session(config=config) as sess:
        # Run the sparse reduction
        sess.run(rl, feed_dict={bm: indices})

def tensor_gpu():
    with tf.device('/gpu:0'):
        # Create a large tensor
        bm = tf.sparse_placeholder(tf.float32)
        rl = tf.sparse_reduce_sum(bm, 1)
    config = tf.ConfigProto(log_device_placement=False)
    config.allow_soft_placement = True
    config.operation_timeout_in_ms = 5000
    with tf.Session(
