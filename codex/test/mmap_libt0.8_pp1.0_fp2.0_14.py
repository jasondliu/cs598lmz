import mmap
import datetime


def write_to_new_file(file_path, site, key_word):
    f = open(file_path, 'w+')
    f.write(site)
    f.write(" ")
    f.write(key_word)
    f.close()


def exists(file_path):
    try:
        f = open(file_path, 'r')
        f.close()
    except IOError:
        return False
    return True


def extract_text(file_path):
    f = open(file_path, 'r')
    data = f.read()
    f.close()
    return data


def create_map(file_path):
    f = open(file_path, 'r')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    i = s.find('{')
    my_data = s[i:]
    f.close()
    return my_data


