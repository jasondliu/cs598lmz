from types import FunctionType
list(FunctionType(fn).__globals__.keys())[:5]

%watermark
%load_ext watermark
%watermark -u -d -p numpy,scipy,sklearn,tensorflow,tqdm
%watermark -v -m -g

# Start IPython cluster
from IPython.parallel import Client
cluster = Client()
cluster.ids

# Execute the same code on all workers
cluster[:].block = True
_ = cluster[:].apply(lambda : "Hello, World")
%timeit sum(cluster[:].apply_sync(lambda: random.random()) for i in range(100))
# Inspect the Engines
import re

def isnotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)

