import gc, weakref, sys

import zope.interface
import zope.component

import z3c.form.interfaces

import z3c.formjs.interfaces

import z3c.zrtresource.interfaces


class Zope3ResourceGenerator(object):
    """
    A utility to collect a set of resources (scripts and stylesheets)
    and generate an html snippet which is to be included in the web page
    to load the resources (by javascript)
    """
    zope.component.adapts(z3c.form.interfaces.IForm)
    zope.interface.implements(z3c.zrtresource.interfaces.IResourceGenerator)

    def __init__(self, form):
        self.form = form

    def update(self):
        self.pagename = self.form.request.get('pagename')
        self.formname = self.form.formname
        self.domain = self.form.request.get('domain', 'default')

    def generate(self):
        resources = {}
        for key
