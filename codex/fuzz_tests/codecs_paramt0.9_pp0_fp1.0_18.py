import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

# Configuration constants.
USER_AGENT = 'vivi.co/browser/0.0.1'
USER_AGENT_CHROMEDRIVER = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

DATA_PATH = 'data'
GROUP_MODELS = 'group_models.txt'
USERS_INDEX = 'users.csv'
USER_DIARY_TEMPLATE = '%Y-%m-%dT%H:%M:%S'
COOKIE_RECORDER = 'cookies.pkl'
COOKIE_RECORDER_BAK = 'cookies_bak.pkl'

DATETIME_FORMAT = '%Y-%m-%d %H:%M'

NUM_ATTEMPTS = 3
NUM_RETRIES = 3

def dt_can_parse
