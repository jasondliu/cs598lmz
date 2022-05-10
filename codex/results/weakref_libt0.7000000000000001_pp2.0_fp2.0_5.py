import weakref
from collections import defaultdict
from collections import namedtuple
from contextlib import contextmanager

from django.conf import settings
from django.db.models import signals
from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _

from . import metadata
from . import settings as elasticsearch_settings
from .exceptions import InvalidIndex
from .signals import post_bulk_index, post_index
from .utils import get_model_name, get_model_class, get_es_model_name

logger = logging.getLogger(__name__)


def _get_indexable_models():
    """
    Returns a dictionary of all models in the project that have an Elasticsearch Index.
    """
    return {
        get_es_model_name(model): model
        for model in apps.get_models()
        if hasattr(model, "search_indexes")
    }


class ElasticsearchIndexRegistry(object):
    def __init__(self):
        self.indexes =
