from bz2 import BZ2Decompressor
BZ2Decompressor
from lxml import etree
from lxml.etree import ElementTree
from lxml.etree import parse
from lxml.etree import tostring
from lxml.etree import XMLSyntaxError
from lxml.etree import XPathEvalError
from os.path import basename
from os.path import dirname
from os.path import exists
from os.path import join
from os.path import relpath
from re import compile as re_compile
from re import escape
from re import match
from re import sub
from subprocess import CalledProcessError
from subprocess import Popen
from subprocess import PIPE
from time import time
from urllib2 import urlopen
from urlparse import urlparse

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.core.management.base import LabelCommand
from django.core.management.base import NoArgsCommand
from django.core.management.base import NoArgsCommand
from django.db.utils import IntegrityError

