import weakref

from threading import Lock

from werkzeug.routing import BaseConverter

from flask import Blueprint, request, session, g, redirect, url_for, abort, \
    render_template, flash, Flask
from flaskext.babel import Babel, gettext

from invenio.base.globals import cfg
from invenio.base.i18n import _
