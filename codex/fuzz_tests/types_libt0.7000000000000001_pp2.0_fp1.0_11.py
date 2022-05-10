import types
types.StringTypes = types.StringType,

import os
import re
import time
import hashlib
import logging
import time
import datetime
import traceback

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from tg2app.lib.base import BaseController, render

from tg2app import model
from tg2app.model import meta

import tg2app.lib.helpers as h


log = logging.getLogger(__name__)


class EventController(BaseController):

    def list(self):
        c.events = meta.Session.query(model.Event).all()
        return render('/events/list.mako')

    def create(self):
        # TODO: add some logic to check if user has permissions to do this
        # TODO: create form validation
        e = model.Event()
        e.name = request.params['name']
        e.description = request.params['description']
        e.start_date
