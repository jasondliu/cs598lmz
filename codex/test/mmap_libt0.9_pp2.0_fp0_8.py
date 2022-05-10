import mmap
import subprocess
from collections import defaultdict
import re
from modules import progress, multiprocessing_utils, file_utils
from modules.objects.gait_cycle import GaitCycle

# GLOBAL VARIABLES #############################################################

# Remove old files from currently running process

runtime_counter=0
model_index=0

# FUNCTIONS ###################################################################

def calc_fft_features(load, draw_plots=False, sample_rate=1000.0, plot_stride=20):

    window = load.create_zero_mean_unit_variance_windowed(500)
    plot_x = np.arange(window.size)
    fft = np.abs(np.fft.fft(window))
    plot_y = fft[np.arange(plot_stride)+1]
    plot_x = plot_x[np.arange(plot_stride)+1]
