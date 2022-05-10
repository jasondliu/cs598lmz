import mmap
import os
import sys
import time

# the file to contain the string to be replaced.
# this should be in the same directory as the script
# to run.
target_file = 'hello_world.py'

# the string to be searched for
old_str = 'Hello World!'

# the string to replace the found string
new_str = 'Hello Again!'

modify_file(target_file, old_str, new_str)

# the output of the file should now say "Hello Again!"
