import mmap
import re

from . import constants

MAX_OFFSET = constants.MAX_OFFSET


def get_offset(file_path, substring):
    with open(file_path, mode="rb") as file:
        file_size = os.path.getsize(file.name)
        if file_size > MAX_OFFSET:
            file_size = MAX_OFFSET
        data = mmap.mmap(file.fileno(), file_size, access=mmap.ACCESS_READ)
        offset = data.find(substring)
        data.close()
    return offset


def get_match_location(file_path, substring):
    offset = get_offset(file_path, substring)
    return offset if offset != -1 else None


def get_first_match(file_path, regex):
    """
        Returns first match of regex in file.
    :param file_path:
    :param regex:
    :return:
    """
    with open(file_path, mode="rb") as file:
        file_size =
