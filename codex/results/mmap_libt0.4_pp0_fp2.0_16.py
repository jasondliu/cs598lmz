import mmap
import os
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import ujson
from django.conf import settings
from django.db import transaction
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext as _

from zerver.lib.actions import (
    do_add_alert_words,
    do_change_user_role,
    do_create_user,
    do_deactivate_user,
    do_reactivate_user,
    do_set_user_display_setting,
    do_set_user_custom_profile_field,
    do_set_user_custom_profile_data_item,
    do_set_user_email_address,
    do_set_user_email_forwarding_address,
    do_set_user_full_name,
    do_set_user_muted_topics
