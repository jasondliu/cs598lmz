import codecs
codecs.register_error('strict', codecs.ignore_errors)

# From https://github.com/leetreveil/pytest-mpl/blob/master/pytest_mpl/plugin.py
# Licensed under BSD
# Adapted by Thomas Robitaille

import os
import shutil
import pytest

from matplotlib import pyplot as plt

# Ensure we have a proper backend (e.g. not a headless one)
plt.switch_backend('agg')

# Set a fixed DPI for the tests
plt.rcParams['savefig.dpi'] = 150


@pytest.fixture(autouse=True)
def mpl_test_settings(request):
    """
    Set some defaults for the tests.
    """
    plt.rcParams['figure.figsize'] = (6.4, 4.8)
    plt.rcParams['font.size'] = 10

    # This line changes the backend of matplotlib, but as of
    # matplotlib 1.5, this is not necessary anymore.

