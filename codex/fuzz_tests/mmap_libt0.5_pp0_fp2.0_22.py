import mmap
import os
import re
import sys
import time
import urllib

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

import config
import model
import util as app_util

class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write(template.render('templates/index.html', {}))


class GetHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write(template.render('templates/get.html', {}))


class GetGroupsHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write(template.render('templates/get-groups.html', {}))


class GetGroupHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write(template.render('templates/get-group.html', {}))


class GetGroupMembersHandler(webapp.
