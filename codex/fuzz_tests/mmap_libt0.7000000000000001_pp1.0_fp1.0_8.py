import mmap
import os
import re
import sys
from subprocess import check_output
import xml.etree.ElementTree as ET
import zipfile

from config import config
from utils import (
    check_and_make_dir,
    prepare_path,
    copy_file,
    save_file,
    move_file,
    rm_file,
    rm_folder,
    run_command,
)


def create_download_path():
    """
    Create download path.
    """
    logging.info('Create download path.')
    check_and_make_dir(config['path']['download'])


def download_file(url, filename):
    """
    Download file from URL.
    """
    logging.info('Download file: ' + filename)
    cmd = 'curl -L -# -o ' + prepare_path(filename) + ' ' + url
    run_command(cmd)


def download_mp4():
    """
    Download all mp4 files from website.
    """
    logging.info('Download mp4 files.'
