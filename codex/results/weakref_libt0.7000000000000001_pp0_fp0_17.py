import weakref

from threading import Lock

from werkzeug.routing import BaseConverter

from flask import Blueprint, request, session, g, redirect, url_for, abort, \
    render_template, flash, Flask
from flaskext.babel import Babel, gettext

from invenio.base.globals import cfg
from invenio.base.i18n import _
from invenio.ext.sqlalchemy import db
from invenio.utils.url import make_user_info_url
from invenio.utils.html import HTMLWasher
from invenio.utils.date import get_time_estimator
from invenio.ext.logging import register_exception
from invenio.ext.login import UserInfo
from invenio.ext.sqlalchemy import current_user
from invenio.ext.principal import identity_changed, Identity
from invenio.ext.mail import send_email
from invenio.ext.sslify import ssl_required
from invenio.modules.accounts.models import
