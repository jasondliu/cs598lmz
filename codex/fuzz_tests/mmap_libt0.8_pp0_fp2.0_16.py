import mmap
import os
import tempfile
import random
import math
import socket

import pytest

from django.core.files.storage import FileSystemStorage
from django.core.files import locks
from django.core.exceptions import ImproperlyConfigured
from django.utils.deconstruct import deconstructible
from django.core.files.base import File, ContentFile
from django.core.files.move import file_move_safe

from . import TemporaryFileStorage


class TestFileStorage(TemporaryFileStorage):
    pass


class TestFileStorage2(TemporaryFileStorage):
    def get_available_name(self, name):
        return super().get_available_name(name) + '2'


@deconstructible
class TestFileStorage3(TemporaryFileStorage):
    pass


class TestFileDescriptor:
    def setup(self):
        self.storage = TestFileStorage2()
        self.filename = 'test_file.txt'
        self.file = ContentFile('custom contents')
        self.file_path = self
