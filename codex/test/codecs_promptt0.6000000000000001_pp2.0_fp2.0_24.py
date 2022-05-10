import codecs
# Test codecs.register_error
# Copyright (C) 2007-2012 by Yann Leboulanger <asterix AT lagaule.org>
# Copyright (C) 2005-2006 Nikos Kouremenos <kourem AT gmail.com>
# Copyright (C) 2006-2012 Jean-Marie Traissard <jim AT lapin.org>
# Copyright (C) 2006 Jonathan Schleifer <js-gajim AT webkeks.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; version 3 only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# encoding: utf-8

import sys
import codecs
import locale
import unittest

