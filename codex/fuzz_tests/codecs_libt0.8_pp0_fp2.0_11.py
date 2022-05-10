import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import cgi
import cgitb
cgitb.enable()

import traceback

import web
from web import form
import config

urls = (
  '/', 'Index',
  '/random', 'Random',
  '/game/(.+)', 'Game',
  '/download/(.+)', 'Download'
)

render = web.template.render('templates/')

login = form.Form(
  form.Textbox('username',
    form.notnull,
    form.regexp('[^\s]+', 'No spaces'),
    form.Validator('Username already exists.', lambda i: i not in config.users),
    description="Username: "),
  form.Password('password',
    form.notnull,
    form.regexp('[^\s]+', 'No spaces'),
    description="Password: "),
  form.Password('password2',
    form.Validator('Passwords do not
