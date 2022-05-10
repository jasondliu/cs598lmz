import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# This file is part of the Metax API service
#
# Copyright 2017-2018 Ministry of Education and Culture, Finland
#
# :author: CSC - IT Center for Science Ltd., Espoo Finland <servicedesk@csc.fi>
# :license: MIT

import logging
import os
import sys
from datetime import datetime
from time import sleep

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import NotFound

from metax_api.api.rest.base.serializers import ValidationError
from metax_api.models import CatalogRecord
from metax_api.models.catalog_record import remove_dataset_from_catalog
from metax_api.models.file import File
from metax_api.models.utils import delete_obj
from metax_api.utils import parse_timestamp
from metax_api
