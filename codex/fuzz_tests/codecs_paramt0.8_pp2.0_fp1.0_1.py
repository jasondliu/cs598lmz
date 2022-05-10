import codecs
codecs.register_error('strict', codecs.ignore_errors)
import os
import sys
import traceback

import CellProfiler.measurement
import CellProfiler.object
import CellProfiler.pipeline
import CellProfiler.workspace
from cellprofiler.preferences import set_headless

set_headless()

import cellprofiler.preferences as cpprefs
from cellprofiler.modules.loadimages import LoadImagesImageProviderURL
from cellprofiler.modules.loadimages import LoadImagesImageProviderHTTPDigest
from cellprofiler.modules.loadimages import LoadSingleImageImageProviderHTTPDigest
from cellprofiler.modules.loadimages import LoadSingleImageImageProviderURL
from cellprofiler.modules.loadimages import LoadImagesImageProvider
from cellprofiler.modules.loadimages import LoadImagesImageProviderHTTPS
from cellprofiler.modules.loadimages import LoadSingleImageImageProvider
from cellprofiler.modules.loadimages import LoadSingleImageImageProviderHTTPS
from cellprofiler.modules.loadimages import C_URL_FOLDER_NAME, C_DISPLAY
