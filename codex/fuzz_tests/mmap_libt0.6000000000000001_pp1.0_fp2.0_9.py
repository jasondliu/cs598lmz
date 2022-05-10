import mmap
import re
import sys
import os
import subprocess

def usage():
    print("Usage: python3 grader.py <test-dir>")
    print("<test-dir> should be the directory containing the test cases.")
    exit(1)

if len(sys.argv) != 2:
    usage()

testdir = sys.argv[1]
if not os.path.isdir(testdir):
    usage()

# Get the list of test cases in the test directory
testcases = [f for f in os.listdir(testdir) if f.endswith(".txt")]
if len(testcases) == 0:
    print("No test cases found in directory %s" % (testdir))
    exit(1)

# Compile the program
compile_process = subprocess.Popen(["g++","-O3","-o","a.out","main.cpp"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = compile_process.communicate()
if compile
