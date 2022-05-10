import codecs
codecs.register_error('strict', codecs.ignore_errors)

import datetime
import json
import os
import re
import subprocess
import sys

import pkg_resources

import six
import yaml

from . import __version__


class ConfigurationError(Exception):
    pass


def _get_data_files():
    if "VIRTUAL_ENV" in os.environ:
        # The virtualenv is active, so use that.
        directory = os.path.join(os.environ["VIRTUAL_ENV"], "share",
                                 "confidant")
    else:
        # The virtualenv is not active, so use the installed location.
        directory = os.path.join(pkg_resources.get_distribution("confidant").location, "share",
                                 "confidant")
    return directory


def _get_config_file():
    # Return the path to the config file.
    if "CONFIDANT_CONFIG" in os.environ:
        return os.environ["CONFIDANT_CONFIG"]
   
