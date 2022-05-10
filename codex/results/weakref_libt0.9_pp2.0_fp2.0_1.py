import weakref

from metropolis import metropolis as met, metropolis as mex
from cdi import cdi
from cdi import common, cdi_package

from cdi import evaluate_type_map, evaluate_type_utils
from cdi import evaluate_type_common

warnings.simplefilter('always')

package_name = cdi.package_name

def type_map_tests():

    # List all modules that are tested in this function

    # Load modules
    typemap, typemap_new, typemap_new_concise = \
        evaluate_type_map.read_whole_type_map(cdi_package)

    # Check all modules
    check_blank_module(typemap)
    check_ambiental_variables_module(typemap)
    check_index_statistics_module(typemap)
    check_indicator_system_module(typemap)
    check_location_values_module(typemap)
    check_item_values_module(typemap)
    check_meteo_module
