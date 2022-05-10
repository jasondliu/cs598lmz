import mmap
import os
import re
import sys


def read_file(filename):
    file_handle = open(filename)
    try:
        return file_handle.read()
    finally:
        file_handle.close()


def read_file_contents(file_handle):
    try:
        return file_handle.read()
    finally:
        file_handle.close()


def read_file_lines(filename):
    file_handle = open(filename)
    try:
        return file_handle.readlines()
    finally:
        file_handle.close()


def read_file_lines_strip(filename):
    lines = read_file_lines(filename)
    return [line.strip() for line in lines]


def write_file(filename, contents):
    file_handle = open(filename, 'w')
    try:
        file_handle.write(contents)
    finally:
        file_handle.close()


def write_file_lines(filename, lines):
    file_handle = open(filename, 'w')

