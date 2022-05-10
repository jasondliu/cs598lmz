import weakref
from jinja2 import Template
from couchdbkit import ResourceNotFound
from dimagi.utils.web import get_url_base, json_handler, parse_int
from dimagi.utils.parsing import json_format_datetime
from dimagi.utils.decorators.datespan import datespan_in_request
from dimagi.utils.dates import DateSpan
from dimagi.utils.couch.database import get_db
from dimagi.utils.couch import get_document_or_not_found
from dimagi.utils.make_uuid import random_hex
from dimagi.utils.couch.undefined import Undefined
from corehq.apps.export.utils import make_export_filename, export_raw
from corehq.apps.app_manager.dbaccessors import get_app, get_brief_apps_in_domain
from corehq.apps.app_manager.models import Application, Form
from corehq.apps.app_manager.suite_xml import SuiteGenerator
