import weakref
from collections import defaultdict
from lxml import etree
from mock import patch

from django.conf import settings
from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.utils import override_settings
from django.utils import timezone

from oioioi.base import tests
from oioioi.base.utils import request_cached
from oioioi.contests.models import (Contest, ProblemInstance, Round,
                                    Submission, SubmissionReport,
                                    UserResultForProblem, UserResultForRound,
                                    submission_statuses)
