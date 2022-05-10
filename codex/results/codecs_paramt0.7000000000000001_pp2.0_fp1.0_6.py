import codecs
codecs.register_error("strict", codecs.ignore_errors)

import logging
import re

from six.moves import html_parser
from six.moves import urllib

from io import BytesIO

try:
    from PIL import Image
    from PIL import ImageFile
except ImportError:
    import Image
    import ImageFile

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage

from olympia import amo
from olympia.amo.utils import (
    chunked, extract_colors_from_image, image_size, img_size, resize_image,
    scale_image, smart_path, walkfiles)
from olympia.amo.templatetags.jinja_helpers import user_media_path
from olympia.translations.utils import to_language


log = logging.getLogger('z.images')
ImageFile.MAXBLOCK = 1024 * 1024 * 100  # 100Mb

# Prefix used for image
