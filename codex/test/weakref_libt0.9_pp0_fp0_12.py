import weakref
from collections import OrderedDict

from bs4 import BeautifulSoup

from olympia.lib.activity.utils import render, save_activity_log
from olympia.amo.templatetags.jinja_helpers import absolutify, urlparams
from olympia import amo
from olympia.amo.models import DynamicBoolField, ManagerBase, ModelBase
from olympia.amo.utils import memoize
from olympia.translations.models import Translation
from olympia.versions.compare import version_int as vint

from .files import File, FileUpload


# TODO: add manager for WebApp objects.


class AddonExcludedRegion(amo.models.ModelBase):
    """This table is used to exclude regions from add-ons."""
    addon = models.ForeignKey(
        'webapps.Webapp', related_name='addonexcludedregion')
    region = models.PositiveIntegerField()

