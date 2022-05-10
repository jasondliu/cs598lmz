import codecs
codecs.register_error('strict', codecs.ignore_errors)

import logging
logger = logging.getLogger(__name__)

import os.path
import re
import sys

import pkg_resources

import yaml

class Loader(yaml.Loader):
    """
    A YAML loader that loads mappings into ordered dictionaries.

    From: https://gist.github.com/844388
    """

    def __init__(self, *args, **kwargs):
        yaml.Loader.__init__(self, *args, **kwargs)

        self.add_constructor(u'tag:yaml.org,2002:map', type(self).construct_yaml_map)
        self.add_constructor(u'tag:yaml.org,2002:omap', type(self).construct_yaml_map)

    def construct_yaml_map(self, node):
        data = OrderedDict()
        yield data
        value = self.construct_mapping(node)
        data.update(value)

    def
