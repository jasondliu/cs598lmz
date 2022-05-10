import _struct
from time import time
from common.logger import Logger

from form.state import State
from form.form_elements import *
from common.utils import get_string_from_bytes
from common.exceptions import *
from ui.colors import *
from ui.menu import Menu

from . import config
from .form_container import FormContainer

logger = Logger(__name__)

class Form(FormContainer):
    """
    Represents form logic
    """
