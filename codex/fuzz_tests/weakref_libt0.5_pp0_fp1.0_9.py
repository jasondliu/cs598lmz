import weakref
import time

from . import Base
from . import DBSession
from . import User
from . import Group
from . import Permission
from . import Role
from . import Route
from . import Resource
from . import RoutePermission
from . import ResourcePermission
from . import GroupRole
from . import UserRole
from . import UserGroup
from . import UserPermission


class BaseController(object):
    """
    Base controller.
    """

    def __init__(self, request):
        self.request = request
        self.dbsession = request.dbsession
        self.user = request.user
        self.current_user = request.current_user


class RootController(BaseController):
    """
    Root controller.
    """

    def index(self):
        """
        Index page.
        """
        return {}


class UserController(BaseController):
    """
    User controller.
    """

    def index(self):
        """
        Index page.
        """
        users = self.dbsession.query(User).all()

