from bz2 import BZ2Decompressor
BZ2Decompressor()

from gzip import GzipFile
GzipFile(fileobj=None, mode=None, compresslevel=None, fileobj=None, mtime=None)
GzipFile.read(size=None)
GzipFile.readline(size=None)
GzipFile.write(data)
GzipFile.writelines(lines)

from tarfile import TarFile
TarFile(name=None, mode=None, fileobj=None, format=None, tarinfo=None, dereference=None, ignore_zeros=None, encoding=None, errors=None, pax_headers=None, debug=None, errorlevel=None)
TarFile.add(name, arcname=None, recursive=None, exclude=None, filter=None, verbose=None, dry_run=None)
TarFile.addfile(tarinfo, fileobj=None)
TarFile.close(force=None)
TarFile.extract(member, path=None, set_attrs=None, numeric_owner=None)
TarFile.extractfile(member)
TarFile.extractall(
