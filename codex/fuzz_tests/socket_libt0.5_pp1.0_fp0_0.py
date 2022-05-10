import socket
import time

from aiohttp import web
from aiohttp_jinja2 import template

from src import config
from src.db import db
from src.models import User
from src.utils.auth import login_required
from src.utils.auth import get_current_user
from src.utils.auth import set_current_user
from src.utils.auth import get_current_session
from src.utils.auth import set_current_session
from src.utils.auth import generate_session
from src.utils.auth import get_session_user
from src.utils.auth import get_session_expiration
from src.utils.auth import get_session_ip
from src.utils.auth import get_session_user_agent
from src.utils.auth import get_session_last_action
from src.utils.auth import get_session_creation
from src.utils.auth import get_session_is_active
from src.utils.auth import get_session_is_valid
from src.utils.auth import is_session_active
from src.utils.auth import is_session_valid
