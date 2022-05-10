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


def get_file_size(file_path):
    """ Получение размера файла по п
