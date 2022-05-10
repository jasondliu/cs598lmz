import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys , os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qsci import *

#===============================
def GetScintilla(fname):
	print "=-"*50
	print "--",fname
	ret = QsciScintilla()
	set_lexer(ret,fname)
	ret.SendScintilla(QsciScintilla.SCI_SETCODEPAGE,65001)
	ret.SendScintilla(QsciScintilla.SCI_SETLEXERLANGUAGE, "Hexadecimal")
	ret.SendScintilla(QsciScintilla.SCI_SETLEXER,QsciScintilla.SCLEX_HEX)
	ret.SendScintilla(QsciScintilla.SCI_SETKEYWORDS,0,"")
	ret.SendScintilla(QsciScintilla.SCI
