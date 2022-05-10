import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import os
from flask import Flask
from flask import Flask, render_template, request, jsonify
from set_db import get_city_id, set_task_id
from get_poi import get_poi
from get_cityid import get_cityid
from get_attractionid import get_attractionid
from get_attractionid import set_attractionid_list
from get_attractionid import set_attractionid_db
from get_attractionid import get_attractionid_list
from get_attractionid import get_attractionid_db
from get_attractionid import get_url_json


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

#redis start
import redis

# 指定redis数据库信
