import io
# Test io.RawIOBase
import subprocess
# Used to pipe command output to stream
import tempfile
# Used to obtain temp file
import stat
# Used to set file permissions

# For debugging purposes, these variables are constructed as lists, even though
# each element applies to a single run (difficult to make a class because of
# command line).
# <type> refers to the type of pipeline. Targets are Assembler, Aligner and
# Variant caller. <value> is a single file or directory.
targets = []  # type: the pipeline that is being run
sources = []  # value: the files/directories to process

# Set the following flags to true when a source has been parsed
file_list_flag = False

pipeline = ""

# TODO: These functions should be in the class


# Test if the given string is a valid file. Return true if valid, false if not
def isfile(path: str, isdir: bool) -> bool:
    # It doesn't make sense to test if a directory is a file, so return true
    if isdir:
        return True

