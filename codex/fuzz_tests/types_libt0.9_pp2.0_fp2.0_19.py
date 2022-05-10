import types
types.ClassType


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[6]:


import numpy as np


# # Part 1: Standard Cell Tracks

# ## Function to plot two cell tracks in same plot

# In[7]:


def plot_tracks(my_tracks, color1, color2, label1, label2, legend_loc='upper right'):
    plt.figure()
    orig_time = np.array(list(my_tracks.keys()))
    orig_x1 = np.array([my_tracks[time]['x1'] for time in my_tracks])
    orig_y1 = np.array([my_tracks[time]['y1'] for time in my_tracks])
    orig_x2 = np.array([my_tracks[time]['x2'] for time in my_tracks])
    orig_y2 = np.array([my_tracks[time]['y2'] for time in my_tracks])
    
