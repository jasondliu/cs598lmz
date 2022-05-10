import mmap
import os
import sys
import time
import re
import glob
import shutil
import subprocess
import tempfile
import traceback
import urllib
import urllib2
import urlparse
import xml.dom.minidom

from optparse import OptionParser
from xml.dom.minidom import parseString

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement

from xml.dom import minidom

from xml.parsers.expat import ExpatError

from os import path
from os.path import join

from sys import platform

from distutils.version import StrictVersion

from shutil import copyfile
from shutil import copytree
from shutil import rmtree

from subprocess import Popen, PIPE
from subprocess import STDOUT

from threading import Thread

from time import sleep

from zipfile import ZipFile

from xml.etree.ElementTree import Element, SubElement

from xml.dom import minidom

from xml.parsers.expat import Exp
