from lzma import LZMADecompressor
LZMADecompressor.max_mem_size = 1024 * 1024 * 1024

path = "F:\\Dataset\\Text\\"

def create_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)

def download_file(url, file_name):
    print("Downloading file: " + url)
    r = requests.get(url, stream=True)
    create_folder(path)

    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

    return file_name

def extract_file(file_name):
    print("Extracting file: " + file_name)
    with open(file_name, 'rb') as f:
        decompressor = LZMADecompressor()
        binary_data = f.read()
        data = decompressor.decompress(binary_data)
       
