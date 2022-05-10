import mmap
import sys
from argparse import ArgumentParser
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterator, List, Tuple, Union

from cephlib.common import CephlabCommand, cephlab_cmd, cephlab_log, log, error
from cephlib.utils.cmd import ce


@dataclass
class Client:
    id: int
    ip: str
    name: str
    fqdn: str
    public_ip: str
    public_fqdn: str
    bdev: str
    fio_job: int
