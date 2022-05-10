import codecs
codecs.register_error('backslashreplace', codecs.backslashreplace_errors)
import re
import os
import sys
import subprocess
import shutil
import tempfile
import arrow
import requests
import json
import logging

DEBUG = False

LOG = logging.getLogger('dlserver')
LOG.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
if DEBUG:
	LOG.addHandler(ch)

__all__ = ['Error', 'EpisodeInfo', 'PyPIDownloader', 'PyPIUploader']


class Error(Exception):
	pass

class EpisodeInfo(object):

	expand_order = ['show', 'id', 'comments', 'releasedate', 'creator', 'release', 'length',
					'description', 'image', 'links', 'chapters']
	'episode release data'

