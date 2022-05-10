import select
# Test select.select
#
# $Id$
#
# Wireshark - Network traffic analyzer
# By Gerald Combs <gerald@wireshark.org>
# Copyright 1998 Gerald Combs
#
# SPDX-License-Identifier: GPL-2.0-or-later
#

import sys

test_fd_table = [
    {
        "Name": "No fds and no timeout",
        "fd_sets": [None, None, None],
        "timeout": None,
        "expected_ret": ([], [], []),
    },
    {
        "Name": "No fds and negative timeout",
        "fd_sets": [None, None, None],
        "timeout": -1,
        "expected_ret": ([], [], []),
    },
    {
        "Name": "No fds and zero timeout",
        "fd_sets": [None, None, None],
        "timeout": 0,
        "expected_ret": ([], [], []),
    },
    {
        "Name": "No fds and positive timeout",
