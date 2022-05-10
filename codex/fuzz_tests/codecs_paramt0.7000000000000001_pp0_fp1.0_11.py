import codecs
codecs.register_error('strict', codecs.ignore_errors)

#---------------------------------------------------------------------------------------------------

class Stemmer:
    """
    This class provides a static method for stemming words/text.
    A word/text is stemmed by removing affixes.
    """
    
    #-----------------------------------------------------------------------------------------------

    @staticmethod
    def stem(word):
        """
        This static method returns the stem of a given word/text.
        """
        
        stem = stemmer.stem(word)
        return stem
    
    #-----------------------------------------------------------------------------------------------

    @staticmethod
    def stemList(wordList):
        """
        This static method returns the stem of a given word list.
        """
        stemList = list(map(lambda word: Stemmer.stem(word), wordList))
        return stemList
    
#---------------------------------------------------------------------------------------------------

class Lemmatizer:
    """
    This class provides a static method for lemmatizing words/text.
    A word/text is lemmatized by grouping together the inflected forms of a word so they can be
    analysed as a single item.
    """
