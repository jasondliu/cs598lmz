import mmap
import os
import re
import sys
import time
from datetime import datetime
from os.path import join

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.timezone import now

from core.models import (
    DataSource,
    DataSourceGroup,
    DataSourceReference,
    DataSourceReferenceType,
    DataSourceReferenceValue,
    DataSourceReferenceValueType,
    DataSourceReferenceValueSet,
    DataSourceReferenceValueSetMember,
    DataSourceReferenceValueSetType,
    DataSourceTag,
    DataSourceTagType,
    DataSourceType,
    DataSourceTypeTagType,
    DataSourceTypeTagTypeMember,
    DataSourceTypeTagTypeMemberType,
    DataSourceTypeTagTypeMemberValue,
    DataSourceTypeTagTypeMemberValueType,
    DataSourceTypeTagTypeMemberValueTypeMember,
    DataSourceTypeTagTypeMemberValueTypeMemberType,
    DataSourceTypeTagTypeMemberValueTypeMemberValue,
    DataSourceTypeTagTypeMemberValueType
