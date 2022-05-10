import mmap
import os
import re
import subprocess
import sys
import tempfile
import time
import traceback
import uuid

import pkg_resources
import six

from mlflow import data
from mlflow.entities import FileInfo
from mlflow.entities.lifecycle_stage import LifecycleStage
from mlflow.entities.run_info import RunInfo
from mlflow.exceptions import MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE
from mlflow.protos.service_pb2 import CreateRun, \
    CreateRun_ExperimentTag, UpdateRun
from mlflow.store import DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH
from mlflow.store.tracking.utils import _get_store
from mlflow.tracking import MlflowClient
from mlflow.tracking.artifact_utils import _download_artifact_from_uri
from mlflow.tracking.client import MlflowHostCreds
from mlflow.tracking.
