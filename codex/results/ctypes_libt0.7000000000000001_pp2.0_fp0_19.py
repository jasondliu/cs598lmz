import ctypes
ctypes.cdll.LoadLibrary('/usr/local/lib/libmagic.so')

class SpellChecker:
    dict = {}

    def __init__(self, file):
        f = open(file, "r")
        for line in f:
            line = line.strip()
            self.dict[line] = True

    def check(self, word):
        return word in self.dict


class PreProcessor:
    def __init__(self):
        self.spellChecker = SpellChecker("../model/dict/dict.txt")
        pass

    def clean(self, sentence):
        sentence = sentence.lower()

        # remove special char
        sentence = sentence.replace('&nbsp;', ' ')
        sentence = sentence.replace('&quot;', '\"')
        sentence = sentence.replace('&amp;', '&')
        sentence = sentence.replace('&lt;', '<')
        sentence = sentence.replace('&gt;', '>')
        sentence = sentence.replace('&ldquo;', '\"')
        sentence =
