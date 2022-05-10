import bz2
bz2.decompress(open("data/enwiki-latest-pages-articles.xml.bz2").read())

from gzip import GzipFile
GzipFile("data/twitter.json.gz").read()

from zipfile import ZipFile
ZipFile("data/twitter.zip").read("twitter.json")

from tarfile import TarFile
TarFile("data/twitter.tar").read("twitter.json")

from lzma import LZMAFile
LZMAFile("data/twitter.json.xz").read()

################################################################################
# Filepaths and filenames
################################################################################

from pathlib import Path
Path("twitter.json").read_text()

# glob, matching file glob patterns

from glob import glob
glob("*.py")
glob("twitter_*.json")
glob("*")

import re
re.compile("^twitter.*\.json$")


# Alternative: OS path manipulation
from os import listdir
listdir(".")

from os.path import splitext, split, exists, isdir, join,
