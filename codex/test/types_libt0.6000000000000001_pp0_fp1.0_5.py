import types
types.ModuleType.get_mplstyle = get_mplstyle

# Make sure that we can find the custom rc file
rc_file = 'pyplot.rc'
if not os.path.isfile(rc_file):
    rc_file = os.path.join(os.path.dirname(__file__), rc_file)

# Load the custom rc file if it exists
if os.path.isfile(rc_file):
    with open(rc_file, 'r') as f:
        mpl.rcParams.update(mpl.rcParamsDefault)
        mpl.rc_file_defaults()
