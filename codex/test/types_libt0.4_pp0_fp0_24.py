import types
types.SimpleNamespace

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.colors import ListedColormap
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
import sympy as sp
from sympy.utilities.lambdify import lambdify
import emcee
import corner
from IPython.display import HTML
import os
from datetime import datetime
import sys
from pathlib import Path

# %%
# import my own modules
sys.path.append('../src')
from ode_models import sir_model, seir_model, sir_model_with_vaccination, seir_model_with_vaccination
from plot_utils import plot_sir, plot
