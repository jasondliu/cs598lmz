import types
types.ModuleType.__path__.__setitem__(0, 'C:\\Users\\user\\Desktop\\dagster-google\\dagster_google\\google')

from __future__ import absolute_import, division, print_function

import sys
import unittest

import mock

from google.cloud import bigquery

from six import reraise

from dagster import (
    DependencyDefinition,
    Field,
    InputDefinition,
    OutputDefinition,
    PipelineDefinition,
    SolidInvocation,
    execute_pipeline,
    lambda_solid,
    pipeline,
    solid,
)
from dagster.core.definitions.executor import ExecutorDefinition, default_executors
from dagster.core.definitions.resource import ResourceDefinition
from dagster.core.execution.api import create_execution_plan, execute_plan
from dagster.core.instance import DagsterInstance
from dagster.core.storage.pipeline_run import PipelineRun, PipelineRunStatus
from dagster.core.storage.type_storage import TypeStoragePluginRegistry

