import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np

class FieldCanvas(FigureCanvas, TimedAnimation):
    def __init__(self, freq_func, voltage_func, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax1 = fig.add_subplot(111)
        self.ax1.set_title('Magnetron $V$ and $f$')
        self.ax1.set_xlabel('Time (s)')
        self.ax1.set_ylabel('Frequency (Hz)')
        self.ax2 = self.ax1.twinx()
        self.ax2.set_ylabel('Voltage (V)')

        self.freq_func = freq_func
        self.voltage_func = voltage_func
        self.freq_line, = self.ax1.plot([], [], lw=2, label='Frequency (Hz)')
       
