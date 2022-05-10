import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# *** Interlock module site-dependent values ***

# Interlock server address
InterlockServerAddr = ('localhost', 0)

# *** Interlock default values for config vars ***

InterlockVarDefaults = {
    # Directory for storing event and status log files
    'evlogdir': os.path.join(os.getcwd(), 'logs'),
    # Directory for storing status files
    'rwdir': os.path.join(os.getcwd(), 'site'),
    # Granularity (in seconds) at which to check status directory
    'rwdir_checktime': 0.1,
    # Granularity (in seconds) at which to write status files
    'rwdir_writetime': 1.0,
    # File pattern for reading stati files
    'rwdir_in_pattern': '*',
    # File pattern for writing status files
    'rwdir_out_pattern': '*',
    # File pattern for reading event files

