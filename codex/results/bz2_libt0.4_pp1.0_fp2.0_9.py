import bz2
bz2.BZ2File(filename).read()

# gzip
import gzip
gzip.open(filename, 'rb').read()

# zipfile
import zipfile
zipfile.ZipFile(filename).read(filename)

# tarfile
import tarfile
tarfile.open(filename).extractall()

# subprocess
import subprocess
subprocess.call(['ls', '-l'])
subprocess.check_output(['ls', '-l'])

# glob
import glob
glob.glob('*.py')

# os.path
import os
os.path.abspath(path)
os.path.basename(path)
os.path.dirname(path)
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)
os.path.join(path1, path2)
os.path.getatime(path)
os.path.getmtime(path)
os.path.getctime(path)
os.path.getsize(
