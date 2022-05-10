import weakref
from collections import defaultdict
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Type,
    cast,
)

from flask import (
    Blueprint,
    Flask,
    Request,
    Response,
    _request_ctx_stack,
    current_app,
    g,
    request,
)
from flask.views import MethodViewType
from flask_restx import Api as BaseApi
from flask_restx.api import Namespace
from flask_restx.fields import Raw
from flask_restx.model import Model
from flask_restx.utils import unpack
from flask_restx.validation import ValidationError
from werkzeug.datastructures import FileStorage
from werkzeug.exceptions import HTTPException
from werkzeug.routing import Rule

from . import __version__
from .auth import Auth
from .config import Config
from .doc_parser import create_doc_parser
from .exceptions import (
    Authentication
