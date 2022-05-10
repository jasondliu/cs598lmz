import lzma
lzma.open

def list_files(path):
    # returns a list of names (with extension, without full path) of all files
    # in folder path
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files

def check_file_is_valid(file_name):
    # returns if file is in valid format
    if(file_name[-2:] == '.x'):
        return True
    return False

def import_files(path):
    # returns a list of all valid files in folder path
    files = []
    raw_files = list_files(path)
    for i in range(len(raw_files)):
        if(check_file_is_valid(raw_files[i])):
            files.append(raw_files[i])
    return files

def remove_extension(file_name):
    return file_name[:-2]

