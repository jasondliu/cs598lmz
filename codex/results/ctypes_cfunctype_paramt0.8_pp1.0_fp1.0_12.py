import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def callback(x):
    print('value of x: {0}'.format(x))
    return x*3
f = FUNTYPE(callback)
print(f(3))

import logging
logging.getLogger('mpl').setLevel(logging.ERROR)


def the_function_to_plot(x):
    return x*x
x = np.arange(-5.0, 5.0, 0.02)
y = the_function_to_plot(x)

plt.plot(x, y, label='function to plot')

ax = plt.gca()
marker, = ax.plot([0], [0], marker='D', color='red', label='marker')

plt.gcf().canvas.mpl_connect('button_press_event', on_click)

plt.ylim(-10, 10)
plt.xlim(-10, 10)

plt.legend(loc='upper right')
plt.grid(True
