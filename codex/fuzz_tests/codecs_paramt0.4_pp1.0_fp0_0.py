import codecs
codecs.register_error('ignore', codecs.ignore_errors)

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Load the API key
api_key = config['DEFAULT']['api_key']

# Load the API endpoint
api_endpoint = config['DEFAULT']['api_endpoint']

# Load the API version
api_version = config['DEFAULT']['api_version']

# Load the API method
api_method = config['DEFAULT']['api_method']

# Load the API parameters
api_parameters = config['DEFAULT']['api_parameters']

# Load the API method
api_method = config['DEFAULT']['api_method']

# Load the API parameters
api_parameters = config['DEFAULT']['api_parameters']

# Load the API method
api_method = config['DEFAULT']['api_method']

# Load the API parameters
api_parameters = config['DEFAULT']['api_parameters']

# Load the API
