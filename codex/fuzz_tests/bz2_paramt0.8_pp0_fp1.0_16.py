from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: bytes('')

import FuzzyFilePath
import FuzzyFilePath.FuzzyFilePath as FFP
import unittest

def get_file_paths(directory):
    return [FFP.FuzzyFilePath('.'.join(f.strip().split('.')[:-1])) for f in os.listdir(directory)]

def construct_test_function(test_case):
    """Returns a function that tests a given test_case with the correct input
    and output files."""
    def test_function(self):
        input_text = open(test_case.input_file_path, 'rb').read().decode('utf-8', errors='replace')
        output_text = open(test_case.output_file_path, 'rb').read().decode('utf-8', errors='replace')
        try:
            test_output = FFP.FuzzyFilePath.fuzzily_find_file_path(input_text)
        except FFP.FuzzyFilePathNotFoundException:
            return

