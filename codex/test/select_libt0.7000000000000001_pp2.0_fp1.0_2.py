import selector
from utils import *

# -------------------------------------------------
# --------------PULSE ANALYSIS---------------------
# -------------------------------------------------

# N is the number of points in the waveform
N = 1 << 15

def get_pulse_amplitude(pulse_ts, window_size=50):
    """
    returns the amplitude of the pulse by calculating the gradient of the signal in the window_size
    :param pulse_ts: np.array of the pulse
    :param window_size: window_size for the gradient
    :return: amplitude of the signal
    """
