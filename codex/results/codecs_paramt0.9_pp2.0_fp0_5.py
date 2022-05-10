import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set default encoding
reload(sys)
sys.setdefaultencoding(encoding)

# Echo texts
file_name = 'echo_txt.txt'

# Original text encoding
source_encoding = 'utf-8'

# Destination encoding
dest_encoding = 'utf-8'


"""
Set the logger
"""
logger = logging.getLogger('echo')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s:%(name)s:%(levelname)s: %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


"""
Read the data from text file
"""


def read_data():
    return read_txt_data(file_
