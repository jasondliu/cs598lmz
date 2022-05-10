import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors='replace_with_space') as f:
        lines = f.readlines()
        return lines

def write_file(file_path, lines):
    with open(file_path, "w", encoding="utf-8", errors='replace_with_space') as f:
        f.writelines(lines)

def get_file_list(dir_path, file_list):
    if os.path.isfile(dir_path):
        file_list.append(dir_path)
    elif os.path.isdir(dir_path):
        for s in os.listdir(dir_path):
            new_dir = os.path.join(dir_path, s)
            get_file_list(new_dir, file_list)
    return file_list

def get_file_list_by_ext(dir_path, file_list, ext):

