import socket
from contextlib import contextmanager
from dataclasses import dataclass, field
from logging import getLogger, StreamHandler, DEBUG
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
from unittest import TestCase

from aiohttp.test_utils import TestClient
from yarl import URL

from neuro_sdk import Config, Container, ContainerStatus, Image, Labels, Volume, \
    VolumeType
from neuro_sdk.clients import BaseClient, Client
from neuro_sdk.exceptions import RequestError
from neuro_sdk.utils import _get_logs_from_container_by_id
from neuro_sdk.version import __version__

from neuro_cli import main
from neuro_cli.config import Config as ConfigCli, ConfigFile
from neuro_cli.formatters import format_datetime
from neuro_cli.root import get_parser
from neuro_cli.utils import _get_config_path

from .utils import find_free_port, run_cli

LOGGER = get
