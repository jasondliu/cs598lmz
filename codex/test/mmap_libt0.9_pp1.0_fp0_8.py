import mmap
import re

def return_pattern(pattern, file_path):
    """search pattern in binary file"""
    pattern = str.encode(pattern)
    try:
        with open(file_path, 'rb') as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            if mm.find(pattern) != -1:
                return mm.find(pattern)
    except:
        print('Error in matching the pattern {}'.format(pattern))

    return 0

def return_values(file_path, start_regex, end_regex):
    """Return values in between start and end regex"""
    new_list = []
    start_pattern = return_pattern(start_regex, file_path)
    end_pattern = return_pattern(end_regex, file_path)

    if start_pattern == end_pattern == 0:
        return []

