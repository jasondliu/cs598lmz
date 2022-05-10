import mmap
import re
import sys
import os
import subprocess

def usage():
    print("Usage: python3 grader.py <test-dir>")
    print("<test-dir> should be the directory containing the test cases.")
    exit(1)

