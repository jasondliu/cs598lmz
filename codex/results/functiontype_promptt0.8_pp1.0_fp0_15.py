import types
# Test types.FunctionType
#
# @author: jbao@redhat.com
#
# @date:   2012-04-6
#
# @description: 
#
# Test Case_id:
#
# Test Case_title:
#
# Input:
#               vda2               first disk
#               --type=raw
#               --souce file://...
#               --storage-format=
#
# Test Step:
#
# Procedure:
# 1. get type of a python function
#
#  
# Expect Results:
#
#
# Issues:
#


import os,sys
import pxssh
import re


def createLog(testname):
    logfile = os.getcwd() + "/" + testname + ".log"
    print "Generating log file: " + logfile
    return open(logfile,'w')


def send_expect(child, command, expect):
    #child.sendline(command)
    #child.expect(expect)
    #print "child.before: " + child.before
   
