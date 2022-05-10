import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import v1

from . import utils
from . import cmd
from . import csv_
from . import dbf_
from . import xml_
from . import gml_
from . import geojson_
from . import ogr
from . import osr
from . import osr_ct
from . import ogr_srs
from . import ogr_srs_ct
from . import ogr_feature
from . import ogr_featurestyle
from . import ogr_field
from . import ogr_geom
from . import ogr_layer
from . import ogr_spatialref
from . import ogr_sql
from . import ogr_sql_ct
from . import ogrtest
from . import ogr_utils
from . import ogr_vrt
from . import ogr_wrap
from . import ogr_wrap_ct
from . import osr_wrap
from . import osr_wrap_ct
from . import pymod
from . import swig_runtime
from . import vector
from
