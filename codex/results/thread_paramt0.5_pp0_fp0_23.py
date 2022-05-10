import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100)))))

#%%
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_plot(i):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x + i)
    plt.cla()
    plt.plot(x, y)

fig = plt.figure()
ani = FuncAnimation(fig, animate_plot, interval=1)
plt.show()

#%%
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("twitter-out.txt","r").read()
    lines = pullData.split('\n')

    xar =
