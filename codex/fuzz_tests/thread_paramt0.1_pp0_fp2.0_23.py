import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from IPython.display import HTML

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from IPython.display import display

from matplotlib import animation, rc
from IPython.display import HTML

from matplotlib.widgets import Slider, Button, RadioButtons

import matplotlib.pyplot as plt
import numpy as np

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from IPython.display import HTML

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from IPython.display import display

from matplot
