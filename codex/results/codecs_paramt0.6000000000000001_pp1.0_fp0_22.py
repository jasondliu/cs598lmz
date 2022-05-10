import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _unicode(s):
    return s if isinstance(s, unicode) else s.decode('utf-8', 'strict')

def _bytes(s):
    return s.encode('utf-8')

def _str(s):
    return _bytes(s) if isinstance(s, unicode) else s

def _get_save_path(save_dir, url):
    if not save_dir:
        return None

    url_parts = urlparse.urlparse(url)
    save_dir = os.path.abspath(save_dir)
    path = os.path.join(save_dir, url_parts.netloc, url_parts.path.lstrip('/'))
    if not os.path.exists(path):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
    return path

def _download_to_file(url, save_
