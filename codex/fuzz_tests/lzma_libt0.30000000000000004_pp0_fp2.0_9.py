import lzma
lzma.open("/dev/null")

import bz2
bz2.open("/dev/null")

import zlib
zlib.open("/dev/null")

import tarfile
tarfile.open("/dev/null")

import zipfile
zipfile.open("/dev/null")

import gzip
gzip.open("/dev/null")

import zipimport
zipimport.zipimporter("/dev/null")

import pkgutil
pkgutil.get_data("/dev/null", "/dev/null")

import pkg_resources
pkg_resources.resource_string("/dev/null", "/dev/null")

import pkg_resources
pkg_resources.resource_stream("/dev/null", "/dev/null")

import pkg_resources
pkg_resources.resource_filename("/dev/null", "/dev/null")

import pkg_resources
pkg_resources.resource_exists("/dev/null", "/dev/null")

import pkg_resources
pkg_resources.resource_isdir("
