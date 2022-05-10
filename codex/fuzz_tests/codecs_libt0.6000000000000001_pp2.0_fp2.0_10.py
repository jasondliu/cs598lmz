import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from flask import Flask, request, session, g, redirect, url_for, \
	 abort, render_template, flash, jsonify
from flask_oauth import OAuth
from flask_login import (LoginManager, current_user, login_required,
												 login_user, logout_user, UserMixin, AnonymousUserMixin,
												 confirm_login, fresh_login_required)
from flask_assets import Environment
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Message, Mail
from flask_cache import Cache
from flask_wtf.csrf import CsrfProtect
from flask_babel import Babel
from flask_babel import lazy_gettext as _l
from flask_babel import gettext as _

import os, sys, re
from datetime import dat
