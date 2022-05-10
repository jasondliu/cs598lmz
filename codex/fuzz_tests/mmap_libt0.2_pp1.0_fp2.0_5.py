import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib2
import zipfile

from os import path

from build_tools import (
    BuildError,
    BuildOptions,
    BuildStep,
    BuildTool,
    BuildToolChain,
    BuildToolStep,
    BuildToolStepResult,
    BuildToolStepResultCode,
    BuildToolStepResultOutput,
    BuildToolStepResultOutputType,
    BuildToolStepResultOutputValue,
    BuildToolStepResultOutputValueType,
    BuildToolStepResultValue,
    BuildToolStepResultValueType,
    BuildToolStepValue,
    BuildToolStepValueType,
    BuildToolValue,
    BuildToolValueType,
    CommandLine,
    CommandLineFlag,
    CommandLineFlagType,
    CommandLineOption,
    CommandLineOptionType,
    CommandLineValue,
    CommandLineValueType,
    File,
    FileType,
    FileValue,
    FileValueType,
    Path,
    PathValue,
    PathValueType,
