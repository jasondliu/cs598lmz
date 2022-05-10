import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connector using pymysql
import pymysql
pymysql.install_as_MySQLdb()

# For image processing
import PIL
from PIL import Image

# For date and time
import datetime

# Other
import json
import random
import time
import urllib.parse
import requests

# Import from app
from app import app
from app.models import db
from app.models.user import User
from app.models.user_token import UserToken
from app.models.user_like import UserLike
from app.models.user_follow import UserFollow
from app.models.user_follow_request import UserFollowRequest
from app.models.user_pin import UserPin
from app.models.user_flag import UserFlag
from app.models.user_feedback import UserFeedback
from app.models.user_block import UserBlock
from app.models.user_mute import UserMute
from app.models
