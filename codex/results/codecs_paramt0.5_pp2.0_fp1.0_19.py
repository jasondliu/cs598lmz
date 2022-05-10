import codecs
codecs.register_error('ignore', codecs.ignore_errors)

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Q
from django.utils.text import slugify

from core.models import *
from data.models import *
from data.utils import *
from data.utils.importer_utils import *
from data.utils.import_utils import *
from data.utils.validator_utils import *
from data.utils.validator_utils import validate_citation_text
from data.utils.validator_utils import validate_citation_url
from data.utils.validator_utils import validate_date
from data.utils.validator_utils import validate_datetime
from data.utils.validator_utils import validate_decimal
from data.utils.validator_utils import validate_email
from data.utils.validator_utils import validate_file_extension
from data.utils.validator_utils import validate_geojson
from data.utils.validator_utils import validate_image_extension
from data.
