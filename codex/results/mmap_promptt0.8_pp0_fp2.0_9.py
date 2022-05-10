import mmap
# Test mmap.mmap() callable
mmap.mmap(0, 1, "foo", "bar")

import msilib
# Test msilib.GetTables() callable
msilib.GetTables()

import msvcrt
# Test msvcrt.getch() callable
msvcrt.getch()

import netrc
# Test netrc.netrc() callable
netrc.netrc()

import new
# Test new.instance() callable
new.instance()

import nis
# Test nis.cat() callable
nis.cat("foo")

import nntplib
# Test nntplib.NNTP() callable
nntplib.NNTP("foo")

import operator
# Test operator.add() callable
operator.add()
# Test operator.concat() callable
operator.concat("foo", "bar")
# Test operator.contains() callable
operator.contains("foo", "bar")
# Test operator.countOf() callable
operator.countOf("foo", "bar")
# Test operator.del
