from lzma import LZMADecompressor
LZMADecompressor= LZMADecompressor # Pyflakes.

from twisted.python.filepath import FilePath
from twisted.python.zipstream import ZipFile as ZFP


class ZipFile(ZFP):
    """
    An implementation of L{IArchive} that can be used to read from a zip file.
    """

    def list(self):
        """
        Get a list of the paths of files in a zip file.
        """
        listing = {}
        for info in self.fp.infolist():
            parts = FilePath(info.filename).split()
            path = parts[0]
            if len(parts) > 1:
                listing.setdefault(path, []).append(info)
            else:
                listing[path] = [info]
        return listing


    def extract(self, path, targetFile):
        """
        Extract a file from the zip file and write it to the target file
        specified.

        @param path: The path of the file to extract.
        @param targetFile: An open file object to which the file should be
            written
