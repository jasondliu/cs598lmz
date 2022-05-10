import mmap
import json
from . import log

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO


def pjoin(*paths):
    return os.path.normpath(os.path.join(*paths))


def get_dict_from_str(str_content, key_type=str, value_type=str, separator='='):
    """
    将一个字符串按照一定格式解析成字典
    :param str_content:
    :param key_type:
    :param value_type:
    :param separator:
    :return:
    """
    dict_data = dict()
    for line in str_content.split('\n'):
        if separator not in line:
            continue
        key, value = line.split(separator, 1)
        dict_data[key_type(key)] = value_type(value)
    return dict_data


def write_
