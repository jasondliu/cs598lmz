import codecs
codecs.register_error('ignore', codecs.ignore_errors)

class Comment:
    def __init__(self, comment, nbLines):
        self.comment = comment
        self.nbLines = nbLines

class CommentList:
    def __init__(self,commentList):
        self.commentList = commentList

class CommentParser(object):

    def __init__(self, comment_type, comment_start, comment_end):
        self.comment_type = comment_type
        self.comment_start = comment_start
        self.comment_end = comment_end
        self.comment_list = []

    def parseFile(self, filename):
        comment = None
        nbLines = 0
        comment_list = []
        try:
            with codecs.open(filename, encoding='utf-8', errors='ignore') as f:
                i = 0
                for line in f:
                    i += 1
                    if line.find(self.comment_start) >= 0:
                        if comment is None:
                            comment = line[line.find(
