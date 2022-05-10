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
    def __init__(self, title, form_id, form_type, form_version, form_content=None, form_content_raw=None, script_text=None, script_hash=None, *args, **kwargs):
        """
        :param title: Form title
        :param form_id: Form id
        :param form_type: Form type
        :param form_version: Form version
        :param form_content: Form content as json
        :param form_content_raw: Form content as binary
        :param script_text: Form script text
        :param
