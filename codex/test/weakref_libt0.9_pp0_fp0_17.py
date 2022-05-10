import weakref

class Stream:
    """Stream abstruction for text. Can be string, bytes, or even a file
    """
    def __init__(self, text, position=0):
        self.text = text
        self.position = position
    def peek(self):
        return self.text[self.position]
    def next(self):
        rtn = self.text[self.position]
        self.position += 1
        if self.position > len(self.text) - 1:
            raise StopIteration
        return rtn

class Regex:
    def __init__(self, pattern, rex=None):
        self.pattern = pattern
        if rex == None:
            self.rex = re.compile(self.pattern)
        else:
            self.rex = rex
    def parse(self, stream):
        """parse a stream with the form of this Regex"""
        return re.match(self.rex, stream.text)
