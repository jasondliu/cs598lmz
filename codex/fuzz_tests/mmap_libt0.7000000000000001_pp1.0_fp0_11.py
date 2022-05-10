import mmap
import os
import re
import sys
import xml.etree.ElementTree as ET

import jinja2

import utils

def main(args):
    # get all available modules
    modules = []
    for path in args.path:
        for module in utils.get_modules(path):
            if module not in modules:
                modules.append(module)

    # get variables for each module
    variables = {}
    for module in modules:
        variables[module] = utils.get_variables(args.path, module)

    # get defaults for each module
    defaults = {}
    for module in modules:
        defaults[module] = utils.get_defaults(args.path, module)

    # get types for each module
    types = {}
    for module in modules:
        types[module] = utils.get_types(args.path, module)

    # get min version for each module
    min_versions = {}
    for module in modules:
        min_versions[module] = utils.get_min_version(args.
