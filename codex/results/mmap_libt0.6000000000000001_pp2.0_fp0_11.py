import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

import pkg_resources

from . import __version__
from . import utils
from . import config

__all__ = ['build', 'build_docker_image', 'build_tarball', 'build_wheels',
           'clean', 'DockerBuildEnvironment']

# The name of the directory containing the source
SOURCE_DIR = 'source'
# The name of the directory into which the wheel will be built
WHEEL_DIR = 'wheelhouse'
# The name of the directory into which the sdist will be built
SDIST_DIR = 'dist'
# The name of the directory containing the Dockerfile for the build
DOCKERFILE_DIR = 'docker'
# The name of the file containing the Dockerfile for the build
DOCKERFILE_NAME = 'Dockerfile'
# The name of the directory containing the docker context
DOCKER_CONTEXT_DIR = 'docker_context'
# The name of the directory containing the docker context
DOCKER_CONTEXT_NAME
