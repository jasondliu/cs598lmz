import threading
threading.stack_size(1024*1024)

#initialize all the variables
x = np.zeros((50, 1))
y = np.zeros((50, 1))
batch_size = 16
num_batches = 50
m = batch_size * num_batches

# make a loop in python using a thread
def load_data():
    for b in range(num_batches):
        for i in range(batch_size):
            x[b*batch_size + i] = np.random.rand(1)
            y[b*batch_size + i] = np.random.rand(1)

t = threading.Thread(target=load_data)
t.start()
# t.join()

#

#placeholders
X = tf.placeholder(tf.float32, shape=(None, 1), name='X')
Y = tf.placeholder(tf.float32, shape=(None, 1), name='Y')

# model
W = tf.get_variable('W', shape=(1, 1), initializer=tf.random_
