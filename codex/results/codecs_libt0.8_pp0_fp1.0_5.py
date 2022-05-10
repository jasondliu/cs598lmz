import codecs
codecs.register(codecs.lookup('idna'))

# Python Imports
import warnings

# Third Party Imports
import math
import pytest

# Project Imports
import jacquard.directory.fingerprint as fingerprint
import jacquard.utils.math_utils as math_utils


# A sample fingerprint with a known layout.
TEST_FINGERPRINT = fingerprint.Fingerprint(
    experiment_version=1,
    scheme="sha256",
    min_similarity=0.7,
    threshold=0.2,
    vectors=[
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
        # We have to skip 31 here so that the hex fingerprint includes
        # a 0x3d.
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 32],
    ])


class TestFingerprint(object):
    def test_scheme(self):
        assert TEST_FINGERPRINT.scheme == "sha256"


    def test_exper
