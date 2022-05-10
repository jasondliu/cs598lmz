import types
types.ClassType

import sys
sys.path.append('/home/zjones/spaceman/spaceman')

import spaceman_app

app = spaceman_app.app
app.debug = True

import view
import api

from spaceman_app import db
from spaceman_app import models

from flask import g
from flask.ext.login import current_user

from spaceman_app.models import User
from spaceman_app.models import Space

from spaceman_app.models.user import User
from spaceman_app.models.space import Space
from spaceman_app.models.space_role import SpaceRole
from spaceman_app.models.space_role_type import SpaceRoleType
from spaceman_app.models.space_member import SpaceMember
from spaceman_app.models.space_member_role import SpaceMemberRole
from spaceman_app.models.space_member_role_type import SpaceMemberRoleType
from spaceman_app.models.space_member_role_type_group import SpaceMemberRoleTypeGroup
from spaceman_app
