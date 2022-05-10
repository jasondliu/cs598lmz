import mmap
import numpy as np
import os
import shutil
import struct
from subprocess import Popen, PIPE, STDOUT
import sys
import tempfile
from typing import *


def _run(command: List[str]) -> None:
    p = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    (stdout, stderr) = p.communicate()
    if p.returncode != 0:
        print("Error running command:")
        print(" ".join(command))
        print("STDOUT:")
        print(stdout.decode("utf-8"))
        print("STDERR:")
        print(stderr.decode("utf-8"))
        sys.exit(1)


def _run_in_tmp_dir(command: List[str]) -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        _run(command + [tmp_dir])


def _run_in_tmp_dir_with_stdin(command: List[str],
