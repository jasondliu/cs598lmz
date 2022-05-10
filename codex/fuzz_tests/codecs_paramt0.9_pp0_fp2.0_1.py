import codecs
codecs.register_error('ignore', codecs.lookup('utf-8')[2])

class HBaseTables(object):
    """
        This class contains all the methods for each Table (Connection object)
    """
    CONN_HOST = 'localhost'
    CONN_PORT = 9090

    def __init__(self, host=CONN_HOST, port=CONN_PORT):
        self.host = host
        self.port = port
        # table names
        self.user_table = 'user'
        self.tweet_table = 'tweet'
        self.relation_table = 'relation'
        # column name
        self.user_info_family = 'info'
        self.user_tweet_family = 'tweet'
        self.person_info_family = 'info'
        self.person_tweet_family = 'tweet'
        self.follow_info_family = 'info'
        # row_key
        self.user_prefix = 'user_'
        self.tweet_prefix = 'tweet_'

    def insert_
