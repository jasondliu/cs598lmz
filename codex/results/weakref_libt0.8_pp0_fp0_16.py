import weakref
import json
import logging
import logging.config
import threading
import time
from typing import Callable, Optional, List, Dict, Any

import requests

from . import (
    CHARM_WAIT_TIMEOUT,
    CHARM_INIT_FAIL,
    CHARM_EVENT_REDEPLOY,
    CHARM_EVENT_UNIT_UPDATED,
    CHARM_EVENT_SERVICE_UPDATED,
    CHARM_EVENT_APP_UPDATED,
    CHARM_EVENT_APP_CONFIG_CHANGED,
    CHARM_EVENT_LEADER_SET,
    CHARM_EVENT_PROM_MONITORING_CHANGED,
    CharmEvent,
    AuthInfo,
    CharmEventType,
    HandlerResponse,
    CharmEventTypeGroup,
    CharmEventDB,
    InternalHandlerArgs,
    InternalHandler,
    get_model_name,
)


class CharmEventLoop(threading.Thread):
    """Event loop listens to the event socket and pushes events to the handler."""
