import mmap
import os
import re
import tempfile
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from flask import current_app
from flask_login import current_user
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import StringField, TextAreaField, IntegerField, SelectField, \
    FieldList, FormField, BooleanField, FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Optional, NumberRange, \
    Regexp, ValidationError

from openatlas import app, logger
from openatlas.models.date import Date
from openatlas.models.entity import Entity
from openatlas.models.link import Link
from openatlas.models.node import Node
from openatlas.models.picture import Picture
from openatlas.util.table import Table
from openatlas.util.util import is_authorized, required_group, required_user


class FormBase(FlaskForm):

    def __init__(
