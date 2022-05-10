import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Get the directory where this file is located
SOURCE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("Source location " + str(SOURCE_DIR))

# Flush output port
fftw_lock.init_fftw()
vna_core.Wobbler.DEFAULT_OUTPUT_FILE = os.path.join(os.path.sep, "dev", "shm", "wobbler.bin")

# Start wobbler thread
t_wobbler = vna_core.Wobbler(output_file=vna_core.Wobbler.DEFAULT_OUTPUT_FILE)
t_wobbler.start()

# Start the app
app = vna_gui.ui_controller.UIController()

# Trigger the do_start sequence in the GUI controller
app.do_start(app)
app.start()

