from lzma import LZMADecompressor
LZMADecompressor


def download_and_save_file(url, filename, dirname):
    """
    Download the file at url and save it as filename in dirname.
    If the file already exists, skip the download.
    """
    filepath = os.path.join(dirname, filename)
    if not os.path.exists(filepath):
        data = urlopen(url)
        print("Downloading", filename)
        with open(filepath, "wb") as f:
            f.write(data.read())
    else:
        print("Skipping", filename)


def gunzip_file(filename, dirname):
    """
    Unzip the gzipped file at filename in dirname.
    If the file already exists, skip the unzip.
    """
    filepath = os.path.join(dirname, filename)
    output_filepath = os.path.join(dirname, filename[0:len(filename) - 3])
    if not os.path.exists(output_filepath):
        with gzip.open(filepath, "
