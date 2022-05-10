import types
types.FunctionType = functiontype

################# end of the hack

import matplotlib
# force headless backend; this messes up the DISPLAY variable, though
matplotlib.use("Agg")

try:
    import pyfits as pf
except ImportError:
    import astropy.io.fits as pf

from datetime import datetime
from celery.decorators import task, periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
from django.conf import settings
from django.template.loader import render_to_string
from tardis.tardis_portal.models import Experiment, Dataset, DatasetParameter, \
    ExperimentParameter, ExperimentAuthor, Replica, User, License
from tardis.tardis_portal.ParameterSetManager import ParameterSetManager
from tardis.tardis_portal.email import send_mail
from tardis.tardis_portal.staging import write_uploaded_file_to_dataset
