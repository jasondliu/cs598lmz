import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib.backends.backend_tkagg
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Graphing")
    root.geometry('600x600')

    fig = Figure(figsize=(10, 5), dpi=100)

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # toolbar = NavigationToolbar2TkAgg(canvas, root)
    # toolbar.update()
    # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1
