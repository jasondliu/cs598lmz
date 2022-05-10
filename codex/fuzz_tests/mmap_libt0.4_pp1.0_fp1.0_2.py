import mmap
import os
import sys
import textwrap
import zipfile

from . import __version__
from . import util

class BatchRunner(object):
    """
    This class is responsible for running a set of test cases in batch mode.
    """
    def __init__(self, args, test_cases):
        self.args = args
        self.test_cases = test_cases

    def run(self):
        """
        Run all the test cases.
        """
        if self.args.test_case_filter:
            test_cases = [test_case for test_case in self.test_cases
                          if test_case.name in self.args.test_case_filter]
        else:
            test_cases = self.test_cases

        # Run the test cases and collect the results.
        results = []
        for test_case in test_cases:
            result = test_case.run(self.args)
            results.append(result)

        # Print the results.
        if self.args.verbose:
            self.print_results
