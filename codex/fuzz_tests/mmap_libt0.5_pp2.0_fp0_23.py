import mmap
import os
import re
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import time
import uuid
import warnings

from concurrent.futures import ThreadPoolExecutor
from functools import wraps
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

import docker

from . import (
    constants,
    exceptions,
    helpers,
    objects,
    resources,
    utils,
)

# Typing aliases
DockerClient = docker.DockerClient
DockerContainer = docker.models.containers.Container
DockerNetwork = docker.models.networks.Network
DockerVolume = docker.models.volumes.Volume

# Typing constants
DockerAPIError = docker.errors.APIError
DockerImage = docker.models.images.Image


class DockerContainerManager:
    """
    A class for managing a single Docker container.
    """


