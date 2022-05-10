import socket
import time
import subprocess
import os
import sys
import random
import re
import json
import threading

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import (
    TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, 
    LocationMessage, EventMessage
)
from wechat_sdk.utils import to_text
from wechat_sdk.ext import *
from wechat_sdk.replies import TextReply, ImageReply, VoiceReply, VideoReply, MusicReply
from wechat_sdk.client import WechatAPI
from wechat_sdk.exceptions import WechatException

