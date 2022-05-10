import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Feed(object):
    def __init__(self):
        self.__feed = feedparser.parse('https://www.reddit.com/.rss')
        self.__entries = self.__feed['entries']
        self.__full_text = ''

    def get_entries(self):
        return self.__entries

    def get_full_text(self):
        for entry in self.__entries:
            self.__full_text += entry['title'] + ' ' + entry['summary']
        self.__full_text = self.__full_text.encode('utf-8', 'strict')
        return self.__full_text

    def get_pos_tokens(self):
        pattern = r'''(?x)
        (?:[A-Z]\.)+|\w+(?:-\w+)*|\$?\d+(?:\.\d+)?%?|\.\.\.|[][.,;"'?():-_`]
        '''
        tokens
