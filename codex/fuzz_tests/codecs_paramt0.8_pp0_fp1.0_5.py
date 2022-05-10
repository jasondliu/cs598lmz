import codecs
codecs.register_error("strict", codecs.ignore_errors)

# The API key must be provided and is used to authenticate access.
if 'API_KEY' in os.environ:
    API_KEY = os.environ['API_KEY']

# The API root must be provided and is used to construct API URLs.
if 'API_ROOT' in os.environ:
    API_ROOT = os.environ['API_ROOT']

# The API endpoint must be provided and is used to construct API URLs.
if 'API_ENDPOINT' in os.environ:
    API_ENDPOINT = os.environ['API_ENDPOINT']

# The API version must be provided and is used to construct API URLs.
if 'API_VERSION' in os.environ:
    API_VERSION = os.environ['API_VERSION']

# The API key must be provided and is used to authenticate access.
if 'API_KEY' in os.environ:
    API_KEY = os.environ['API_KEY']

# The API key must be
