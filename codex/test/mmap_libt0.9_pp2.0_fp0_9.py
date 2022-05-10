import mmap
from flask import g
from flask import request
from flask import url_for

from cc.api.resources import api
from cc.api.schemas import UserSchema
from cc.auth import is_responsible_for_user
from cc.auth import Organization
from cc.auth import Permissions
