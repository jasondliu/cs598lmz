import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.TextIOBase
# Test io.BytesIO
# Test io.StringIO
# Test io.BufferedReader
# Test io.BufferedWriter
# Test io.BufferedRWPair
# Test io.BufferedRandom
# Test io.FileIO
# Test io.BytesIO
# Test io.StringIO
# Test io.TextIOWrapper
# Test io.open

# Issue #15208: test the C implementation of io.TextIOWrapper.
import _io
# Test _io.BytesIO
# Test _io.StringIO
# Test _io.TextIOWrapper

# Test the doctests
import doctest
# Test doctest.runtests
# Test doctest.OutputChecker
# Test doctest.DocTestParser
# Test doctest.DocTest
# Test doctest.DebugRunner
# Test doctest.DocTestFinder
# Test doctest.DocTestFinder.find
# Test doctest.DocTestFinder.findall
# Test doctest.DocTestFinder.from
