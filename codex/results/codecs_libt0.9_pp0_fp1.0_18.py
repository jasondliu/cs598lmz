import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def get_indexes(config, is_clementine, index_file='index.json'):
    if os.path.isfile(index_file):
        index = json.load(open(index_file))
    else:
        index = {'indexes': {}}
    index['config'] = config
    search_dirs = [config.MusicDir]
    if os.path.isfile(config.CGALib):
        search_dirs.extend(json.load(open(config.CGALib)))
    for base_dir in search_dirs:
        for dirpath, dirnames, filenames in os.walk(base_dir):
            root, album = os.path.split(dirpath)
            if album:
                if not album in index['indexes']:
                    index['indexes'][album] = {}
                try:
                    song_fnames = sorted(fnmatch.filter(filenames, '*.[
