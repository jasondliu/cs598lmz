import weakref
import re
import os
import sys
import logging
from StringIO import StringIO

from ckan.lib.munge import munge_title_to_name, munge_tag
from ckan.lib.base import request, c
from ckan.model import Session, Package
from ckan.logic import tuplize_dict, clean_dict, parse_params
from ckan.logic import NotFound
from ckan.logic.schema import default_package_schema, package_form_schema
from ckan.logic.action.update import _update_package_relationship
from ckan.logic.action.get import package_show
from ckan.lib.helpers import json
from ckan.lib.navl.dictization_functions import validate, DataError, unflatten
from ckan.plugins import implements, SingletonPlugin, IRoutes, IConfigurer
from ckan.plugins import IConfigurable, IPackageController, IDomainObjectModification
from ckan.plugins import IValidators
from ckan.plugins import ITemplateHelpers

from
