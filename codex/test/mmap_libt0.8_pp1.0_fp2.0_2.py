import mmap
import os
import os.path
import re
import shutil


def make_dirs(dir_name):
    """ Проверка существования директории и её создание в случае отсутствия.

    :param dir_name: путь до директории, котрую необходимо проверить и создать
    :return: None
    """
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)


