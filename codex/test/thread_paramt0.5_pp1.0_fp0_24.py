import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from IPython.display import clear_output

from tqdm import tqdm, trange
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
