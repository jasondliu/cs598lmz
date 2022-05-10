import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Get the path to the data directory
data_path = os.path.join(current_dir, "../data")

# Get the path to the data file
data_file = os.path.join(data_path, "data.json")

# Get the path to the data file
data_file_temp = os.path.join(data_path, "data_temp.json")

# Get the path to the data file
data_file_old = os.path.join(data_path, "data_old.json")

# Get the path to the data file
data_file_new = os.path.join(data_path, "data_new.json")

# Get the path to the data file
data_file_updated = os.path.join(data
