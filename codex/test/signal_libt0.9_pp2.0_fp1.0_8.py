import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # Allow Ctrl-C

# Global settings
cwd = Path.getcwd()
logger = logger.get_logger(__name__)

# Read settings from file
settings = get_project_settings(cwd)

# Directory for plots
plot_dir = get_plots_dir(cwd)

# Meta-information file
meta_file = Path(get_meta_file_path(cwd))
assert meta_file.exists(), f"Meta-information file not found: {meta_file}"

# Load meta-information
meta_dict = meta_load(meta_file)

# Trajectory file
data_file = Path(get_data_file_path(cwd))
if not data_file.exists():
    data_file = None

# Load data
data_dict = data_load(data_file)
if data_dict['N_runs'] < 1:
    data_dict = None

#
# Exported functions
#


