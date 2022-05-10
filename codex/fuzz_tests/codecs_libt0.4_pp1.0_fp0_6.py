import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#%%

def get_data_from_file(filepath):
    all_data = []
    with open(filepath, 'r') as f:
        for line in f:
            line_data = json.loads(line)
            all_data.append(line_data)
    return all_data

#%%

def get_data_from_files(filepaths):
    all_data = []
    for filepath in filepaths:
        all_data.extend(get_data_from_file(filepath))
    return all_data

#%%

def get_data_from_dir(dirpath):
    filepaths = []
    for subdir, dirs, files in os.walk(dirpath):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"):
                filepaths.append(filepath)

