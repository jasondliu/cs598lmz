import lzma
lzma_popen = subprocess.Popen(['lzma', '-7', '-si'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

import gzip
gzip_popen = subprocess.Popen(['gzip', '-7', '-c'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

from typing import Generator
def iter_files(path):
	with os.scandir(path) as files:
		for entry in files:
			if entry.is_file():
				yield entry.path

def zipdir(path: str, zipfile_path: str) -> None:
	from zipfile import ZipFile
	from functools import partial
	with ZipFile(zipfile_path, 'w') as zipf:
		for file in iter_files(path):
			zipf.write(file)

def save_backup
