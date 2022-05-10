import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

from buildbot.process.buildstep import LoggingBuildStep, SUCCESS, FAILURE
from buildbot.status.results import EXCEPTION
from buildbot.steps.source.base import Source
from buildbot.steps.source.git import Git
from buildbot.steps.shell import WithProperties
from buildbot.steps.transfer import FileUpload
from twisted.internet import defer
from twisted.internet import reactor
from twisted.python import log
from twisted.python import runtime
from twisted.python.filepath import FilePath

from mozpack.copier import FileRegistry
from mozpack.errors import errors
from mozpack.files import (
    GeneratedFile,
    DeflatedFile,
    JarFile,
    ManifestFile,
    PreprocessedFile,
)
from mozpack.manifests import (
    InstallManifest,
    UnreadableInstallManifest,
)
from mozpack.packager import (
    SimplePackager,

