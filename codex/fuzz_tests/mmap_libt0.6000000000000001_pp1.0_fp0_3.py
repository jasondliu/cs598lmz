import mmap
import re
import sys

def main(input_file):
    f = open(input_file, 'r')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    # Find the beginning of the first entry
    entry_start = s.find('#START')
    if entry_start == -1:
        print 'No entries found'
        return

    # Find the end of the first entry
    entry_end = s.find('#END')
    if entry_end == -1:
        print 'Unterminated entry'
        return

    # Seek to the start of the first entry
    s.seek(entry_start)

    # Process the first entry
    process_entry(s, entry_end)

    # Loop over the rest of the entries
    while True:
        # Seek to the end of the previous entry
        s.seek(entry_end)

        # Find the beginning of the next entry
        entry_start = s.find('#START')
        if entry_start == -1:
