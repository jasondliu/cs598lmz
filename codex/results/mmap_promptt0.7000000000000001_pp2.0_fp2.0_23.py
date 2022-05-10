import mmap
# Test mmap.mmap with anonymous mapping
#
# This test is known to fail on FreeBSD 8 and earlier versions
# when run with ulimit -v unlimited.  The failure is caused
# by an attempt to allocate a huge mapping, which fails on
# these versions of FreeBSD.

# Copyright (C) 2012, 2013, 2016 Free Software Foundation, Inc.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from support import import_module
mmap_module = import_module('mmap')
