import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() using APSW
import apsw
import zlib
import os

#
# CMakeDependentTestBase class adds support for running tests only when
# a certain dependency was found by CMake's FIND_PACKAGE() macro.
#
# Usage:
#
# In "CMakeLists.txt":
#
# find_package(libfoo)
# if(LIBFOO_FOUND)
#     add_definitions(-DLIBFOO_FOUND)
# endif()
#
# In test source file:
#
# class DefinedIfFooIsPresent(CMakeDependentTestBase):
#     pass
#
# class DefinedIfFooIsNotPresent(CMakeDependentTestBase):
#     pass
#
# class DefinedIfFooIsNotPresent(CMakeDependentTestBase):
#     expected_to_fail_if_defined = True
#
# class DefinedIfFooIsNotPresent(CMakeDependentTestBase):
#     expected_to_fail_if_defined = True
#     expected_to_fail_if_
