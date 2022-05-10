import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    """
    Reads the data from the file.
    """
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def get_data_from_url(url):
    """
    Reads the data from the url.
    """
    data = []
    with urllib.request.urlopen(url) as f:
        for line in f:
            data.append(line.decode('utf-8').strip())
    return data

def get_data_from_url_with_cookie(url, cookie):
    """
    Reads the data from the url.
    """
    data = []
    opener = urllib.request.build_opener()
    opener.addheaders.append(('Cookie', cookie))
    with opener.open(url) as f:
        for line in f:
            data.append(line.decode('utf-
