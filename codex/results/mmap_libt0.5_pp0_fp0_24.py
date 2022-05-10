import mmap
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # create 2 dictionaries
    # one to store the number of times a number has occurred
    # one to store the number of times a number has been used as a factor
    # each time a number is used, check if it has been used as a factor in the past
    # if so, add the number of times it has been used as a factor to the count
    # if the number is the factor of a number that has occured in the past, add it to the second dictionary
    # increment the count of the number of times the number has occurred
    # if the number has occurred in the past, and the number is a factor of a number that has occured in the past, add it to the count
    # if the number is the factor of a number that has occured in the past, add it to the second dictionary
    # increment the count of the number of times the number has occurred
    # return the count
    count = 0
    number_counts = {}
    factor_count
