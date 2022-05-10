from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor()

# https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
def download_file(url, local_filename, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
    return local_filename

def download_and_extract(url, local_filename, extract_path, chunk_size=128):
    download_file(url, local_filename, chunk_size)
    with open(local_filename, 'rb') as f:
        file_content = f.read()
    tar_file = tarfile.open(fileobj=io.BytesIO(file_content))
    tar_file.extractall(extract_path)
    
def download_and_extract_lzma(
