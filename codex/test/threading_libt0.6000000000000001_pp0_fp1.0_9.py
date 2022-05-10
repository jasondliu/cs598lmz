import threading
threading.stack_size(2**27)

class DQN(object):
    def __init__(self, sess, args, env_name, env, input_size, output_size, name='main'):
        self.sess = sess
        self.args = args
        self.env_name = env_name
        self.env = env
        self.input_size = input_size
        self.output_size = output_size
        self.name = name
        self.model_path = self.args.model_path
        self.build_model()

    def build_model(self):
        with tf.variable_scope(self.name):
            self.X = tf.placeholder(tf.float32, [None, self.input_size], name='input')
            self.Y = tf.placeholder(tf.float32, [None, self.output_size], name='label')
            self.Z = tf.placeholder(tf.float32, [None, 1], name='action')

