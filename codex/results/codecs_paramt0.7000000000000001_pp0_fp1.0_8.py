import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Add the import path for the modules in this package
sys.path.append(os.path.dirname(__file__))

# Add the import path for the dependencies (some of which are internal to this package)
# (relative to this file)
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

# Add the import path for the dependencies (some of which are internal to this package)
# (relative to the project root)
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../..'))

# Also some of the dependencies are in the parent directory, which is not
# the parent directory of the project root directory. So we'll add those
# explicitly.
sys
