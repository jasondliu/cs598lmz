import weakref
from datetime import datetime
import time
import json
import logging

from ckan.common import config, request

from ckanext.oauth2provider.model.token import Token as OAuth2Token
from ckanext.oauth2provider.model.client import Client


log = logging.getLogger(__name__)


class OAuth2Plugin(p.SingletonPlugin):
    """
    A plugin to implement OAuth2.
    """

    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IAuthFunctions, inherit=True)
    p.implements(p.IActions, inherit=True)
    p.implements(p.IAuthenticator)
    p.implements(p.IBlueprint)

    def configure(self, config):
        self.ckan_host = config.get('ckan.site_url', '//localhost:5000')
        self.site
