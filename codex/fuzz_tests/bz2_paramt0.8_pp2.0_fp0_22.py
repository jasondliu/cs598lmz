from bz2 import BZ2Decompressor
BZ2Decompressor._BufferSize = 30 * 1024

def _get_tables(data, mydir, cache_dir=None):
    if cache_dir is not None:
        cache_dir = os.path.join(mydir, cache_dir)
        if not os.path.isdir(cache_dir):
            os.makedirs(cache_dir, exist_ok=True)
    for item in data:
        fpath = os.path.join(mydir, item)
        (prefix, suffix) = os.path.splitext(fpath)
        if suffix == '.json':
            continue
        if suffix != '.bz2':
            print("Warning, not handling file "+fpath)
            continue
        if cache_dir is not None:
            cached_fpath = os.path.join(cache_dir, os.path.basename(fpath))
            if os.path.exists(cached_fpath):
                f = open(cached_fpath, 'rb')
            else:
                f = bz2.BZ2File(fpath,
