import bz2
bz2.BZ2File(file)

import gzip
gzip.GzipFile(file)

import lzma
lzma.LZMAFile(file)

import zipfile
zipfile.ZipFile(file)

import tarfile
tarfile.TarFile(file)

import tempfile
tempfile.TemporaryFile(mode='w+b', buffering=0)

import shutil
shutil.make_archive(base_name, format, root_dir, base_dir, verbose, dry_run, owner, group, logger)
shutil.get_archive_formats()
shutil.unpack_archive(filename, extract_dir, format, extra_data)
shutil.unpack_archive(filename, extract_dir, format)
shutil.unpack_archive(filename, extract_dir)
shutil.unpack_archive(filename)

import pathlib
pathlib.Path.cwd()

import glob
glob.glob(pathname)

import fnmatch
fnmatch.fnmatch(filename, pattern)
fnmatch
