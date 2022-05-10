import io
import logging
import re
import time
import traceback

from PIL import Image as pil_image
from PIL import ImageDraw, ImageSequence

from celery import states

from django.conf import settings
from django.utils.translation import install as install_translation

from celery_progress.backend import ProgressRecorder

from .conf import settings as image_settings
from .exceptions import UnknownImageFormat
from .forms import ImageForm
from .models import Image
from .utils import (ImageSize, get_image_dimensions, get_image_ratio, get_image_size, get_exiffield, set_exiffield)

from ._version import __version__
from ._celery import app


__original_queue = app.conf.CELERY_DEFAULT_QUEUE
__original_routes = app.routes


def _prefix_route(name, route):
    return {name: route}

# in case of celerybeat, setup the right queue
if hasattr(settings,'CELERYBEAT_SCHEDULE
