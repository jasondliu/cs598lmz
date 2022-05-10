import _struct
import mmh3
import os
import re
import random
import sys
from struct import unpack

# a bloom filter is a data structure that gives you an approximate (but error-free) answer to a \texttt{contains} query, and
# can use much less memory than if you used a set.
#
# A bloom filter is a list of $M$ bits, initially all 0. We can use any $k$ hash functions
# to map integers to $M$ bits. If we want to add "hello" to a bloom filter, then we will hash "hello" with each
# hash function, and set all of the corresponding bits to 1. If we want to test if the bloom filter contains
# "hello", we will hash "hello" with each hash function, and check if all of the corresponding bits are 1. 
#
# If any bit is 0, then we immediately know that the string has never been added to the set. Otherwise, we can 
# only conclude that "hello" might have been added to the set.

#
# It is possible to implement a bloom filter by a compact representation as well as by a dense
