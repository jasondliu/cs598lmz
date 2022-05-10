import weakref
from pkg_resources import resource_filename
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions

from .. import __version__
from .. import _sage_const_log as log
from ..util import json
from ..util.misc import SageCellVersion
from ..util.temporary_file import atomic_write
from ..util.decorators import sage_wraps, skip_doctest
from ..server.support import (
    get_resource,
    get_sage_cell_version,
    get_sage_cell_version_check,
    get_sage_cell_version_check_url,
    get_sage_cell_version_check_url_html,
    get_sage_cell_version_url,
    get_sage_cell_version_url_html,
    get_sage_cell_version_url_html_escaped,
    get_sage_cell_version_url_text,
    get_sage_cell_version_url_text_escaped,
   
