import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import yaml

import git

import unittest

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.test import TestCase

import pygit2

from fw.models import FW, FWComponent, Release
from fw.models import FWComponentType
from fw.models import FWComponentBranch, FWComponentTypeBranch
from fw.models import Component, ComponentType
from fw.models import ComponentBranch, ComponentTypeBranch
from fw.models import ReleaseComponentType, ReleaseComponentTypeBranch
from fw.models import ReleaseFWComponentType, ReleaseFWComponentTypeBranch

from fw.tests.forms import ReleaseForm, ComponentBranchForm


class FWTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repo = git.Repo.init(os.path.
