import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)

def make_sine_pulse(f):
    """
    Function to create a function that returns a sine pulse
    """
    def sine_pulse(x):
        """
        Function that returns a sine pulse
        """
        return np.sin(2*np.pi*f*x)
    return sine_pulse

def make_gauss_pulse(f):
    """
    Function to create a function that returns a gaussian pulse
    """
    def gauss_pulse(x):
        """
        Function that returns a gaussian pulse
        """
        return np.exp(-x**2)
    return gauss_pulse

# create a sine pulse
sine_pulse = make_sine_pulse(1)

# create a gaussian pulse
gauss_pulse = make_gauss_pulse(1)

# create a random pulse
rand_pulse = lambda x: np.random.randn()

# create a step function

