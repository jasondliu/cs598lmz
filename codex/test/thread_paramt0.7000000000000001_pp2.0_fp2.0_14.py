import sys, threading
threading.Thread(target=lambda: sys.stderr.write('\x1b[2J\x1b[H'),daemon=True).start()

import numpy as np, os, pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
