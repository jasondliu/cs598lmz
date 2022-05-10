import mmap
import contextlib
import typing
import glob
import itertools
import os
import sys
import subprocess


class Tag:
    def __init__(self, tag_id, tag_name, file_name, line_number, qualifier, comment, template_type):
        self.tag_id = tag_id
        self.tag_name = tag_name
        self.file_name = file_name
        self.line_number = line_number
        self.qualifier = qualifier
        self.comment = comment
        self.template_type = template_type

    def __str__(self):
        return (
            f"Tag: tag_id: {self.tag_id}, tag_name: {self.tag_name}, "
            f"file_name: {self.file_name}, line_number: {self.line_number}, "
            f"qualifier: {self.qualifier}, comment: {self.comment}, "
            f"template_type: {self.template_type}"
        )


