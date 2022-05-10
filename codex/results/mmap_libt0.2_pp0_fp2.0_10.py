import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse
import zipfile

from build_artifact import BuildArtifact
from build_options import OPTIONS
from build_paths import BUILD_DIR, OUT_DIR
from build_utils import (BuildLogFile, BuildStep, BuildStepError,
                         CheckoutGitRepo, CheckoutSvnRepo,
                         DownloadAndUnpack, GetHostOsFromPlatform,
                         GetHostArchFromPlatform, GetSdkVersion,
                         GetVersion, GetVersionInt, GetVersionName,
                         GetVersionNameForHostOs, PrintError, PrintWarning,
                         RunCommand, RunCommandInDir, RunCommandWithRetry,
                         RunGit, RunGitWithCode, RunSvn, RunSvnWithCode,
                         RunWithRetry, SetEnvironmentAndGetCoreClrDllDir,
                         SetEnvironmentAndGetRuntimeLibDir,
                         SetEnvironmentAndGetRuntimePath,
                         SetEnvironmentAndGetXunit
