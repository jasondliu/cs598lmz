import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#import pdb

def get_file_paths(root_path):
    """returns a list of file paths in a given directory (and subdirectories)"""
    file_paths = []
    for dir_path, dir_names, file_names in os.walk(root_path):
        for file_name in file_names:
            file_paths.append(os.path.join(dir_path, file_name))
    return file_paths

def get_file_paths_by_ext(root_path, ext):
    """returns a list of file paths in a given directory (and subdirectories) with a given extension"""
    file_paths = []
    for dir_path, dir_names, file_names in os.walk(root_path):
        for file_name in file_names:
            if ext in file_name:
                file_paths.append(os.path.join(dir_path, file
