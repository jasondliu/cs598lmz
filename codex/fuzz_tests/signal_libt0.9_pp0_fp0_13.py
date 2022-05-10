import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# make the shared array to syncronize the simulation with the gui
GUI_SHARED_ARRAY = Array('i', range(2))

# Constants for the GUI_SHARED_ARRAY
RENDER = 0
RUN_SIMULATION_TICK = 1

# Flag set in the thread causing the GUI to close
_STOP_EVENT = threading.Event()
