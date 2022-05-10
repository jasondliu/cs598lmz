import gc, weakref

import numpy as np

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import Spectral6

from bokeh.sampledata.autompg import autompg as df

output_file("toolbar.html")

TOOLS="pan,wheel_zoom,box_zoom,reset,save"

p1 = figure(title="MPG by Year", tools=TOOLS, x_axis_label='Year', y_axis_label='MPG')
p1.circle(x=df['yr'], y=df['mpg'], color=Spectral6[0], size=12, alpha=0.5)

p2 = figure(title="HP vs. Displacement", tools=TOOLS, x_axis_label='Displacement', y_axis_label='HP')
p2.scatter(x=df['displ'], y=df['hp
