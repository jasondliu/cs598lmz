import codecs
codecs.register_error('replace_python', codecs.lookup_error('replace'))

# Global variable to store the path to the configuration file.
config_file = None

# Global variable to store the configuration data.
config = None

# Global variable to store the path to the file containing the last
# version of the data.
version_file = None

# Global variable to store the path to the file containing the last
# version of the data.
version_data = None

# Global variable to store the path to the file containing the data.
data_file = None

# Global variable to store the path to the file containing the data.
data = None

# Global variable to store the path to the file containing the data.
data_backup = None

# Global variable to store the path to the file containing the data.
data_diff = None

# Global variable to store the path to the file containing the data.
data_diff_backup = None

# Global variable to store the path to the file containing the data.
data_diff_temp = None

# Global variable to store the path to the file containing
