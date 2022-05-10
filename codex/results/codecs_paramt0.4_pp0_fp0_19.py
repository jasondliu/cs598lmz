import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  
#-------------------------------------------------------------------------------
class Article(object):
    def __init__(self, title, text, url, date, author, section, comments):
        self.title = title
        self.text = text
        self.url = url
        self.date = date
        self.author = author
        self.section = section
        self.comments = comments

#-------------------------------------------------------------------------------
#  
#-------------------------------------------------------------------------------
class Comment(object):
    def __init__(self, author, text, date, user_url):
        self.author = author
        self.text = text
        self.date = date
        self.user_url = user_url

#-------------------------------------------------------------------------------
#  
#-------------------------------------------------------------------------------
class Parser(object):
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.article = None
        self.comments = []
        self.__get_soup()
        self.__get_article()
        self.__get_comments
