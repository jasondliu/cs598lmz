import weakref
import random
import copy
import logging

import vstruct
import vstruct.defs.windows.vtypes as VSTRUCT_WINDOWS_VTYPES
import vstruct.defs.darwin.vtypes as VSTRUCT_DARWIN_VTYPES

import envi.memory as e_mem
import envi.windows.memory as e_win_mem
import envi.windows.wow64 as e_wow64
import envi.symstore as e_symstore
import envi.config as e_config
import envi.expression as e_expr

from vq.viv_utils.pscan import PagedMemoryObject

import vivisect.const as viv_const
import vivisect.impapi as viv_iapi
import vivisect.analysis.generic as viv_gen
import vivisect.analysis.i386.codeblocks as viv_cb
import vivisect.analysis.i386.anom as viv_i386_anom
import vivisect.analysis.i386.data as viv_i386
