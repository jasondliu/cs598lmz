import weakref
# Test weakref.ref(x)() == x for several types of x.
# Also test weakref.proxy(x) == x for several types of x.
# Also test weakref.getweakrefcount(x)
# Also test weakref.getweakrefs(x)
# Also test weakref.proxy(x)

import weakref
import unittest
import sys
import gc
import operator
import copy
import pickle
import warnings
import types
import os
import re
import struct
import array
import itertools
import collections
import contextlib
import io
import _testcapi
import _weakref
import _collections
import _collections_abc
import _pyio
import _thread
import _threading_local
import _testbuffer
import _testinternalcapi
import _testmultiphase
import _test_multiprocessing
import _test_multiprocessing_fork
import _test_multiprocessing_forkserver
import _test_multiprocessing_main_handling
import _test_multiprocessing_spawning
import _
