import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

from scipy.integrate import odeint
from scipy.optimize import fsolve

from IPython.display import HTML

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from IPython.display import display

from scipy.integrate import odeint
from scipy.optimize import fsolve

from IPython.display import HTML

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from IPython.display import display

from scipy.integrate import odeint
from scipy.optimize import fsolve

from IPython.display import HTML

from ipywidgets import interact, interactive, fixed, interact_manual
import ip
