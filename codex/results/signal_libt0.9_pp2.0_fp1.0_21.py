import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# widget_data = [int(np.random.random()*100) for _ in xrange(6)]
# widget_x = [int(np.random.random()*25) for _ in xrange(6)]
# widget_y = [int(np.random.random()*25) for _ in xrange(6)]
# widget_x_start = np.random.random()*10
# widget_y_start = np.random.random()*10

better_widgets = [[10,10,('button')],
				  [20,10,('button')],
				  [40,10,('button')],
				  [50,10,('button')],
				  [5,5,('button')],
				  [15,5,('button')]]

canvas_height = 27
canvas_width = 55

canvas_buffer_area = 10

####################
# Testing functions

