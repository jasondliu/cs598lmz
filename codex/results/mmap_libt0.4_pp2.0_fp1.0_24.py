import mmap
import os
import re
import subprocess
import sys
import time

from collections import defaultdict

import boto3
import botocore
import pytest

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core.models.trace_header import TraceHeader
from aws_xray_sdk.core.models.xray_error import XrayError
from aws_xray_sdk.core.models import http
from aws_xray_sdk.core.sampling import SamplingStrategy
from aws_xray_sdk.core.sampling.local.rule_cache import RuleCache
from aws_xray_sdk.core.sampling.local.sampling_rule import SamplingRule
from aws_xray_sdk.core.sampling.local.sampling_rule_manager import SamplingRuleManager
from aws_xray_sdk.core.utils.compat import get_function_arguments
from aws_xray_sdk.core.utils.
