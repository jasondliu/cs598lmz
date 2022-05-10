import mmap
import sys
import h5py

#===============================================================================
#                     FUNCTIONS
#===============================================================================

#===============================================================================
# FUNCTION: get_data
#===============================================================================
#
# PURPOSE: Reads in all the data in the binary file and returns the data as an
#          array. Will also return the data size in bytes, and the data type,
#          and the L1a_file info (gain, start time, record length, etc).
#
# INPUT:   file_name = String; name of the .dat file you want to read in.
#          telem = String; the name of the telemetry that you want the data for
#                       (ex: 'ENG_TEMP_C')
#          vars = String; The name of the variable that you want the data for
#                      (ex: 'msct_rate')
#
# NOTES:   1) Function will read in data only for the given telem and vars.
#          2) The function will first check if 'telem' is specified and if so
#             it will read in the telemetry
