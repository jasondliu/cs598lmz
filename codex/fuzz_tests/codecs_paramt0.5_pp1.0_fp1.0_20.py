import codecs
codecs.register_error('strict', codecs.ignore_errors)

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

from bson.json_util import dumps

from utils import get_db
from utils import get_collection

from utils import get_user_from_request
from utils import get_user_from_token

from utils import get_user_info

from utils import get_user_from_id

from utils import get_user_from_name

from utils import get_user_from_email

from utils import get_user_from_username

from utils import get_user_from_token

from utils import get_user_from_request

from utils import get_user_from_id

from utils import get_user_from_name

from utils import get_user_from_email

from utils import get_user_from_username

from ut
