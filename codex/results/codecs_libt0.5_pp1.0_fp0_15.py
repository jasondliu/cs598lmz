import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Initialize the plotly FigureWidget class
fig = go.FigureWidget()

# Initialize the plotly FigureWidget class
fig2 = go.FigureWidget()

# Initialize the plotly FigureWidget class
fig3 = go.FigureWidget()

# Initialize the plotly FigureWidget class
fig4 = go.FigureWidget()

# Define the callback function: update_plot
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = x_select.value
    y = y_select.value
    z = z_select.value
    # Label axes of plot
    fig.layout.xaxis.title = x
    fig.layout.yaxis.title = y
    # Set new_data
    new_data = {
        'x': df[df['Year'] == yr][x],
        'y': df[df['Year']
