import mmap
import sys

from common import (
    set_of_matches_from_file,
    make_sets_for_all_matches,
    sorted_set_of_matches,
    set_of_all_matches,
    remove_duplicates_from_set,
)


def get_number_of_lines_in_file(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    fp.close()
    return lines


def write_to_file(file_path, unique_lines):
    with open(file_path, "w") as file:
        for line in unique_lines:
            file.write(line + "\n")


def remove_lines_from_file(file_path, unique_lines):
    all_lines = set_of_all_matches(file_path)
    unique_lines_from_file = remove_dupl
