import bz2
bz2.BZ2File.write = None


def _extract_archive(file_path, path='.', archive_format='auto'):
    """Extracts an archive if it matches tar, tar.gz, tar.bz, or zip formats.

    Args:
        file_path (str): path to the archive file
        path (str): path to extract the archive file
        archive_format (str): Archive format to try for extracting the file.
            Options are 'auto', 'tar', 'zip', and None.
            'tar' includes tar, tar.gz, and tar.bz files.
            The default 'auto' is ['tar', 'zip'].
            None or an empty list will return no matches found.

    Returns:
        False if a non-compressed archive format is tried.
    """
    if _extract_tar(file_path, path):
        return True
    if _extract_zip(file_path):
        return True
    return False

def _extract_tar(file_path, path='.'):
    """Extracts a tar
