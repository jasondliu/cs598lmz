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
%time _ = run_batch_session(10, 10, 10)

reset_graph()
benchmark_file = "build/dlc_bellman_benchmark.tsv"
%time bench_mark(benchmark_file)
 
########################################################################
# now plot the results

benches=[]
policies=[]

with open(benchmark_file, 'rt') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    for row in tsvin:
        #print row
        if len(row) < 2:
