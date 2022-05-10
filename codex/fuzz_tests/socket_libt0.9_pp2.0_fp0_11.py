import socket
import struct
import sys

class Hangman:

    def __init__(self):
        self.HANGMAN_PHRASES = ['apple', 'banana', 'cherry', 'dragonfruit'
                                ,'elderberry', 'fig', 'guava', 'honeydew'
                                ,'imbe', 'jackfruit']
        self.randPhraseIdx = random.randint(0, len(self.HANGMAN_PHRASES)-1)
        self.guessedChars = []
        self.lives = 6
        self.correctWord = self.HANGMAN_PHRASES[self.randPhraseIdx]
        self.prtLettersArr = self.createPrintLetterArr(self.correctWord)

    def createPrintLetterArr(self, word):
        lArr = []
        for l in word:
            lArr.append("_")
        return lArr

    def updatePrintLetterArr(self, word, guess):
        idx = 0
        while idx < len(
