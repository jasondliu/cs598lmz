import mmap
# Test mmap.mmap for reading
import os
# Required for the mmap module to work
import re
# Used for regular expressions
import string
# Import string module for string manipulation
import time
# Import time to track execution time
import urllib
# Used for urlencode
import urllib2
# Used for sending internet requests
import webbrowser
# Used for opening URLs in the default browser


def main():

    # Initialize variables
    words = []
    # This list will contain all of the words in the file
    words_counted = []
    # This list will contain all of the words that were counted
    words_counted_counts = []
    # This list will contain the number of instances each word appears
    words_not_counted = []
    # This list will contain all of the words that were not counted
    words_not_counted_counts = []
    # This list will contain the number of instances each word appears

    # Initialize counters
    word_counter = 0
    # This will count the number of words added to words_counted
    word_counter_index = 0
    #
