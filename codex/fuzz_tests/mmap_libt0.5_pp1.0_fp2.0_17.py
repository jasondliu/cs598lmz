import mmap
import os
import re
import shutil
import subprocess
import time

from . import utils

DISK_TEMPLATE = '''#!/bin/bash

set -e

# This is a template for creating a disk image.
#
# The disk image will be created in the current directory, with the name
# specified in the 'DISK_IMAGE' environment variable.
#
# The disk image will contain a single partition, formatted as ext4.

# The size of the disk image, in bytes.
DISK_SIZE=%(disk_size)d

# The size of the partition, in bytes.
PARTITION_SIZE=$((DISK_SIZE - %(partition_offset)d))

# Create a blank disk image.
dd if=/dev/zero of="$DISK_IMAGE" bs=1 count=0 seek=$DISK_SIZE

# Create a partition table.
parted -s "$DISK_IMAGE" mklabel msdos

# Create a single partition.
parted -s "$DISK_IMAGE" unit b mkpart
