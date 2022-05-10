import weakref

import django.forms
from django import forms


class FilterTemplate(object):
    def __init__(self, name, field_class):
        self.name = name
        self.field_class = field_class

class Filter(object):
    def __init__(self, template, data):
        if not isinstance(data, dict):
            raise AttributeError("Filter data must be a dictionary")
        self._template = template
        self._data = data
    
    @property
    def name(self):
        return self.template.name
    
    @property
    def template(self):
        "This template can contain restrictive settings which are not changeable."
        return self._template
    
    @property
    def data(self):
        "This property is the data dictionary associated with this filter."
        return self._data
    
