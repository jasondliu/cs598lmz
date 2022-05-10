from lzma import LZMADecompressor
LZMADecompressor()

def get_file_name(url):
    return url.split('/')[-1]

def get_file_size(file_name):
    return os.path.getsize(file_name)

def download_file(url, file_name, use_proxy=True):
    if use_proxy:
        proxy = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
        r = requests.get(url, proxies=proxy)
    else:
        r = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(r.content)
    print('Downloaded {}'.format(file_name))

def download_file_with_progress(url, file_name, use_proxy=True):
    if use_proxy:
        proxy = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
        r = requests.get(url, proxies=proxy
