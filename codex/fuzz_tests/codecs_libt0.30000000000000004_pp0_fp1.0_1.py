import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import traceback
from flask import Flask, request, abort, render_template, jsonify, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.expression import case
from sqlalchemy.sql.expression import func
from sqlalchemy.sql.expression import desc
from sqlalchemy.sql.expression import asc
from sqlalchemy.sql.expression import literal_column
from sqlalchemy.sql.expression import bindparam
from sqlalchemy.sql.expression import tuple_
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.expression import or_
from sqlalchemy.sql.expression import exists
from
