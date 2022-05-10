import mmap
import re
import os
import os.path

from .. import config

class Importer(object):

    def __init__(self):
        pass

    def __call__(self):
        self.import_all()
        
    def import_all(self):
        self.import_python()
        self.import_roles()
        self.import_permissions()

    def import_python(self):
        # TODO: make this only import what is needed
        import flask
        import flask.ext
        import flask.ext.sqlalchemy
        import flask.ext.admin
        import flask.ext.login
        import sqlalchemy
        import sqlalchemy.orm
        import flask.ext.admin.contrib.sqlamodel

    def import_roles(self):
        #import the roles
        map(do_import, config.ROLES)

    def import_permissions(self):
        #import the permissions
        map(do_import, config.PERMISSIONS)

def do_import(module_name):
    __import
