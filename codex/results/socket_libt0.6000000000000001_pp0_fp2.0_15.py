import socket
import urllib.request
import urllib.error
import urllib.parse
import os

from .common import InfoExtractor
from ..utils import (
    compat_urllib_parse,
)


class GenericIE(InfoExtractor):
    """Generic last-resort information extractor."""
    _VALID_URL = r'.*'
    IE_DESC = 'Generic downloader that works on some sites'
    _TEST = {
        'url': 'http://www.youtube.com/watch?v=BaW_jenozKc',
        'file': 'BaW_jenozKc.flv',
        'info_dict': {
            "title": "Stacy's Mom",
            "uploader": "FountainsOfWayneVEVO",
            "uploader_id": "FountainsOfWayneVEVO",
            "upload_date": "20070521",
        },
        'params': {
            # rtmp download
            'skip_download': True,
        },
    }

    def report_download_
