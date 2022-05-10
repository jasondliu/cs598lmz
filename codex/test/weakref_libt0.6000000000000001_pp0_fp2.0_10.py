import weakref
import threading

import openmc
import openmc.checkvalue as cv

_thread_local = threading.local()

_statepoint_filename = 'statepoint.{0:04}.binary'
_summary_filename = 'summary.h5'
_tallies_filename = 'tallies.{0:04}.h5'
_source_filename = 'source.{0:04}.h5'
_geometry_filename = 'geometry.xml'
_materials_filename = 'materials.xml'
_settings_filename = 'settings.xml'
_tallies_xml_filename = 'tallies.xml'
_plots_xml_filename = 'plots.xml'
_nuclides_xml_filename = 'nuclides.xml'
