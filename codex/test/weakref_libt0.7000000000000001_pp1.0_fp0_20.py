import weakref

from gi.repository import Gtk
from gi.repository import XApp

from softwarecenter.backend.channel import Channel
from softwarecenter.backend.channel import CHANNEL_PREFIX
from softwarecenter.db.application import Application

from softwarecenter.ui.gtk3.models.appstore2 import AppDetailsStore
from softwarecenter.ui.gtk3.widgets.appdetails import (
    get_app_details_for_app,
    get_app_details_for_pkgname,
    get_app_details_for_channel_name,
)
from softwarecenter.ui.gtk3.widgets.appdetails import AppDetailsViewGtk
from softwarecenter.ui.gtk3.widgets.spinner import SpinnerNotebook
from softwarecenter.ui.gtk3.widgets.spinner import SpinnerNotebookPage
from softwarecenter.utils import ExecutionTime
from softwarecenter.utils import OnlyOne
from softwarecenter.utils import utf8

from softwarecenter.backend.reviews import ReviewStats
