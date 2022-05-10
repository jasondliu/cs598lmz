import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Ensure we can import models from the app
current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '..'))

from app import db, models
from app.models import *

from sqlalchemy import func, or_

from datetime import datetime, timedelta
from dateutil.parser import parse

from flask import current_app

from app.utils import *
from app.constants import *
from app.helpers import *

from app.services.app_engine import AppEngine

from app.services.analytics import Analytics
from app.services.analytics import AnalyticsException
from app.services.analytics import AnalyticsTotalsException
from app.services.analytics import AnalyticsTotals
from app.services.analytics import AnalyticsTotalsPeriod
from app.services.analytics import AnalyticsTotalsPeriodException
from app.services.analytics import Analytics
