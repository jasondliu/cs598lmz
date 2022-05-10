import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.optimize import minimize

from sklearn.metrics import mean_squared_error

from IPython.display import HTML

import warnings
warnings.filterwarnings('ignore')

# %matplotlib inline

# %config InlineBackend.figure_format = 'retina'

plt.style.use('ggplot')

np.random.seed(42)

# # SEIR Model

# ## Model

# In[2]:


def seir_model(y, t, beta, gamma, sigma, N):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
