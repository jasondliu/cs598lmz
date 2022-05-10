import types
types.FunctionType.__module__ = '__fake__'

import sys
sys.modules['__fake__'] = sys.modules['__builtin__']

import re
import urllib2
import cgi
import json
import argparse
import logging

from os import path
from os import environ
from os import getcwd

from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

from jinja2 import Environment
from jinja2 import FileSystemLoader

import maven_downloader
import maven_downloader.util

from maven_downloader.downloader import Downloader
from maven_downloader.downloader import Repository

from maven_downloader.mvn import Mvn
from maven_downloader.mvn import read_pom

from maven_downloader.maven import Maven

from maven_downloader.dependency import Dependency
from maven_downloader.dependency import DependencyTree
