import mmap
from flask import g
from flask import request
from flask import url_for

from cc.api.resources import api
from cc.api.schemas import UserSchema
from cc.auth import is_responsible_for_user
from cc.auth import Organization
from cc.auth import Permissions
from cc.auth import User
from cc.database.pagination import Pagination
from cc.database.pagination import paginate_query
from cc.database.utils import as_dict
from cc.models import UserMixin

# The maximum number of users to import at one time.
MAX_IMPORT_SIZE = 512


def _create_user(
    username, password=None, is_admin=None, organization_ids=None, permissions=None
):
    user = User(username=username)

    if password is not None:
        user.set_password(password)

    if is_admin is not None:
        user.admin = is_admin

    for organization_id in organization_ids or ():
        organization = Organization.query.get(organization_id)
        if
