import mmap
import os
import re
import sys
import time
import urllib2
import xml.dom.minidom

import jinja2
import webapp2

import config
import model
import util


class BasePage(webapp2.RequestHandler):
  def __init__(self, *args, **kwargs):
    super(BasePage, self).__init__(*args, **kwargs)
    self.template_values = {}

  def render_template(self, template_name, **kwargs):
    self.template_values.update(kwargs)
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = jinja_environment.get_template(template_name)
    self.response.out.write(template.render(self.template_values))


class StatsPage(BasePage):
  def get(self):
    stats = {}

