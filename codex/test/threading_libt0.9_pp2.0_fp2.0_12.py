import threading
threading.stack_size(2**28)

import pyximport
pyximport.install()

# Suppress some of the more annoying error messages
import warnings
warnings.filterwarnings("ignore")

# Always good to reset a few things
def reset_graph(seed=42):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)

########################################################################
# now run the file

reset_graph()
