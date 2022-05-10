import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib
import urllib2
import zipfile

from optparse import OptionParser

from android_build_system import get_build_var, get_out_dir, get_target_arch, \
    get_build_tools_version, get_build_tools_dir, get_android_sdk_root, \
    get_android_sdk_build_tools_dir, get_android_sdk_platform_tools_dir, \
    get_android_sdk_tools_dir, get_android_sdk_version, get_android_sdk_api_level, \
    get_android_sdk_ndk_version, get_android_sdk_ndk_api_level, \
    get_android_sdk_ndk_platform, get_android_sdk_ndk_toolchain_version, \
    get_android_sdk_ndk_toolchain_prefix, get_android_sdk_ndk_toolchain_
