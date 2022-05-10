import gc, weakref
import datetime, time

from lib.image_utils import ImageFilter

from app import config
from lib.sane import scanner
from lib.sane_initializer import sane_initializer
from tasks.shared import initialize_worker
from thumbnailer import Thumbnailer, process_url

from ..models import Photo
from ..utils import run_async
from ..exceptions import PhotoAlreadyExistsError

log = logging.getLogger(__name__)

batch_scanning_enabled = True

try:
    from ..scan import scanner, get_thumbnail, get_pil_image
except ImportError:
    batch_scanning_enabled = False
    log.info('Photo batch scanning is disabled. Install pysane and scan-tools to enable.')


class InvalidPhotoError(Exception):
    """
    Indicates a problem with the image that prevents it from being uploaded.
    """
    pass


@lru_cache(maxsize=config.thumbnail_cache_max)
def get_thumbnail_cache(url):
    # url is checked at the beginning of handler
