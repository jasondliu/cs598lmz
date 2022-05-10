import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
from datetime import datetime
import time

from flask import jsonify, request
from flask_restplus import Resource, fields, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from .. import api
from ..util import serializer
from . import db, images
from .models import User
from .helpers import (
    get_user_from_email,
    get_user_from_id,
    get_user_from_username,
    get_user_from_token,
    get_friends,
    get_friend_requests,
    get_pending_requests,
    get_users_not_friends,
    get_user_by_location,
    get_user_by_interest,
    get_user_by_birthday,
    get_user_by_gender,
    get_user_by_sexuality,
    get_user_by_name,
    get_
