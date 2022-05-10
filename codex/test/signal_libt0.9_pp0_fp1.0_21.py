import signal
signal.signal(signal.SIGTERM, sig_term_handler)

##########################################
# AWS
##########################################

os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '/app/credentials'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

##########################################
# BOTO
##########################################

# default region
boto3.setup_default_session(region_name='us-east-1')

# logging
boto_logger = logging.getLogger('boto3')
boto_logger.setLevel(logging.CRITICAL)
boto_logger.addHandler(logging.StreamHandler())

# set the user agent
# boto3.DEFAULT_USER_AGENT = "boto3:{}".format(boto3.__version__)

##########################################
# Werkzeug
##########################################

