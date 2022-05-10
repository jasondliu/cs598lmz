import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.patches import Rectangle
from matplotlib import rc

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties

fig = plt.figure(1)

def add_relative_value_labels(ax, spacing=5):
    for i, patch in enumerate(ax.patches):
        height = patch.get_height()
        if height > 0:
            ax.text(patch.get_x()+patch.get_width()/2., height + spacing, \
                    '%d'%(height), ha="center") 
        else:
            ax.text(patch.get_x()+patch.get_width()/2., height - spacing, \
                    '%d'%(height), ha="center") 

def add_absolute_value_labels(ax
