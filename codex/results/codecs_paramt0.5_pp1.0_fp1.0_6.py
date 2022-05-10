import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_songs_from_file(path, encoding='utf-8'):
    songs = []
    with codecs.open(path, 'r', encoding=encoding, errors='strict') as f:
        for line in f:
            songs.append(line.strip())
    return songs

def get_songs_from_dir(path, encoding='utf-8'):
    songs = []
    for filename in os.listdir(path):
        if not filename.endswith('.txt'):
            continue
        with codecs.open(os.path.join(path, filename), 'r', encoding=encoding, errors='strict') as f:
            for line in f:
                songs.append(line.strip())
    return songs

def get_songs(path, encoding='utf-8'):
    if os.path.isfile(path):
        return get_songs_from_file(path, encoding)
    elif os.path.isdir(path):
        return get
