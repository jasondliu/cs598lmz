import socket
import sys
import threading
import time
import traceback
from typing import Any, Dict, List, Optional, Tuple

import main
from common.constants import Constants
from common.data_object.json_builder.base import BaseBuilder
from common.data_object.json_builder.environment import EnvironmentBuilder
from common.data_object.json_builder.execution import ExecutionBuilder
from common.data_object.json_builder.machine import MachineBuilder
from common.data_object.json_builder.test_case import TestCaseBuilder
from common.data_object.json_builder.test_suite import TestSuiteBuilder
from common.data_object.json_dto import (
    Machine,
    TestCase,
    TestSuite,
    TestSuiteExecution,
    TestSuiteExecutionReport,
    TestSuiteReport,
)
from common.data_object.json_parser.execution_report_parser import ExecutionReportParser
from common.data_object.json_parser.machine_parser import MachineParser
from common.data_object.json_parser.test
