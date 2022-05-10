import io
# Test io.RawIOBase
#
# This tests the RawIOBase implementation of the io module.
# Note that the io module provides an abstract base class
# for Raw I/O, so normally you would not import it directly.
#
# Written by Amaury Forgeot d'Arc and Antoine Pitrou

import os
import sys
import unittest
import io

