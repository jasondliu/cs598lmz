import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

import os, time, random

#=======================================================================
#
#  Written by:  Joty Terpereau
#
#=======================================================================

#=======================================================================
#
#  This script runs the experiment with the parameters specified below.
#  The experiment consists of running a number of jobs.
#
#  The number of jobs is:
#      nVars * nProcs * nReps
#
#  The script creates a directory for each job and runs the job in that directory.
#
#  The results are saved in a .csv file in the directory where this script is run.
#
#  The script needs the following files:
#
#  - job.sh
#  - run.sh
#  - job.pbs
#  - job.jdf
#  - job.mjd
#
#  The file job.sh runs the job.
#  The file run.sh runs the program.
#  The files job.pbs, job.jdf, and job.mjd are the
