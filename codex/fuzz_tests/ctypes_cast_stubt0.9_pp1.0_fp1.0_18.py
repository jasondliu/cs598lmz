import ctypes
ctypes.cast(0, ctypes.py_object)

dll = None

is32Bit = (ctypes.sizeof(ctypes.c_void_p) == 4)

if is32Bit:
    dll = ctypes.cdll.LoadLibrary("../OpenSimRoot/builds/Release/OpenSimMoko.dll")
else:
    dll = ctypes.cdll.LoadLibrary("../OpenSimRoot/builds/ReleaseWin64/OpenSimMoko.dll")

# ------------------------------------------------------------------------------------------------------
#   Start: user-defined variables
# ------------------------------------------------------------------------------------------------------
adaptationType = "none"  # the type of adaptation performed by this script.  Available: "none", "proprioception", and "trajectory".

# The following parameters are used only when adaptationType == "proprioception".
adaptationStart = 5 # the simulation time (in seconds) when adaptation begins
adaptationEnd = 7 # the simulation time (in seconds) when adaptation ends
afterLearningStart = 7 # the simulation time (in seconds) when the perturbation is removed and the tested is asked to perform the movement again

