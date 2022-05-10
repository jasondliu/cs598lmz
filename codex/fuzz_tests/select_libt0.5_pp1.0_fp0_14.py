import select
import socket
import sys
import threading
import time
import traceback
import urllib
import urlparse
import uuid

import pkg_resources

from jenkins_jobs.builder import Builder
from jenkins_jobs.registry import ModuleRegistry
from jenkins_jobs.xml_config import XmlJob, XmlView
from jenkins_jobs.errors import (JenkinsJobsException,
                                 MissingJenkinsAPI,
                                 JenkinsAPIException,
                                 JenkinsAuthException)
from jenkins_jobs.xml_config import XmlJob
from jenkins_jobs.xml_config import XmlView
from jenkins_jobs.xml_config import XmlPluginManager
from jenkins_jobs.xml_config import XmlViewList
from jenkins_jobs.xml_config import XmlSidebar
from jenkins_jobs.xml_config import XmlViewList
from jenkins_jobs.xml_config import XmlSidebar
from jenkins_jobs.xml_config import XmlUserList
from jenkins_jobs.
