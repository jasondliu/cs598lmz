import lzma
lzma.check_input = lambda x: True
import json
from flask import (render_template, flash, Blueprint, request, session, redirect, url_for,
                   send_from_directory)
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from hashlib import sha256
import base64
from werkzeug.utils import secure_filename
from app import app
from app.models import UserAuth
from app.models import EncryptionKey
from app.models import Backup
from app.models import get_user_data, content_encryption_key, encrypt
from app.sheet import new_user_sheet
import os
import time


main = Blueprint('main', __name__)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


def prompt_user(upload_file_alias, token, key, user_id, sheet_id):
    if sheet_id == 'none':
        sheet_
