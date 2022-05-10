import codecs
# Test codecs.register_error()
import sys
import tempfile
import unittest
import warnings


def get_codecs():
    write_support = []
    read_support = []
    non_working = set()
    for name in codecs.__all__ + ['utf-8-sig']:
        if name in non_working:
            continue
