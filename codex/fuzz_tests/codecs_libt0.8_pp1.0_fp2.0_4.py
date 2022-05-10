import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import pyodbc
import datetime
import sys
import traceback

###################################################################################################
#
# Changelog:
#
#	2014-09-02	MR		Initial Version
#	2014-10-05	MR		createNoExcelFiles()
#	2014-10-22	MR		createNoExcelFiles()
#	2014-10-29	MR		createNoExcelFiles()
#	2014-12-05	MR		createNoExcelFiles()
#	2014-12-16	MR		createNoExcelFiles()
#	2015-01-09	MR		createNoExcelFiles()
#	2015-02-02	MR		createNoExcelFiles()
#	2015-02-03	MR		createNoExcelFiles()
#	2015-03-24	MR		createNoExcelFiles()
#	2015-06-08	MR		createNoExcelFiles()

