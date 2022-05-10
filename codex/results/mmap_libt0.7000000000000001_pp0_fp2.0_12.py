import mmap
from colorama import Fore
import sys
import os

FILE_PATH = "./output/result.txt"
TARGET_PATH = "./output/result.txt"

# TODO: Display in a pretty way
# TODO: Display the number of results and the number of results per page.
# TODO: Display the results starting from the page that has been requested.


class SearchEngine(object):

    def __init__(self, path):
        self.path = path
        self.file = None
        self.text = ""
        self.index = 0
        self.result_pages = []

    def open_file(self):
        self.file = open(self.path, "r")

    def read_file(self):
        self.text = self.file.read()

    def close_file(self):
        self.file.close()

    def create_indexes(self, word):
        indexes = []
        position = 0
        while True:
            position = self.text.find(word, position)
            if position == -1:
               
