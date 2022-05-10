import mmap
import re

def get_file_content(file_path):
    with open(file_path, 'r+') as f:
        return mmap.mmap(f.fileno(), 0)

def get_line_number(file_content, pattern):
    return [m.start() for m in re.finditer(pattern, file_content)]

def get_line_content(file_path, line_number):
    with open(file_path, 'r+') as f:
        return f.readlines()[line_number]

def get_line_content_by_pattern(file_path, pattern):
    file_content = get_file_content(file_path)
    line_number = get_line_number(file_content, pattern)
    return get_line_content(file_path, line_number[0])

def get_line_count(file_path):
    with open(file_path, 'r+') as f:
        return len(f.readlines())

def get_line_count_by_pattern(
