import types
types.ClassType = type

from fred_webadmin.controller.adif.adif import AdifController
from fred_webadmin.translation import _
from fred_webadmin.corba import ccReg
from fred_webadmin import config
from fred_webadmin.corba import Registry, ccReg
from fred_webadmin.utils import DateTime
from fred_webadmin.webwidgets.gpyweb.gpyweb import WebWidget, attr, div, table, td, th, tr, a, tbody, thead, span, img, script, div
from fred_webadmin.webwidgets.details.details import Details
from fred_webadmin.webwidgets.utils import Error, Info, Warning
from fred_webadmin.webwidgets.forms.base import Input
from fred_webadmin.webwidgets.details.adif import AdifDetails
from fred_webadmin.webwidgets.forms.adif import AdifForm
